from pathlib import Path
from typing import Dict, List, Optional, Type, TypeVar, Generic, Any, Callable, cast
import time
from gql.utils.reader import read_csv_files_to_polars_df
from gql.utils.logger import get_logger
from gql.utils.utility import check_file_path, normalize_path_for_spark

logger = get_logger(__name__)

T = TypeVar('T')

class DataService(Generic[T]):
    """Service for loading and caching data from CSV files."""
    
    def __init__(
        self, 
        path: str, 
        entity_type: Type[T],
        transform_func: Callable[[Dict[str, Any]], T],
        cache_ttl_seconds: int = 300
    ):
        """
        Initialize the data service.
        
        Args:
            path: Path to the CSV files
            entity_type: The type of entity this service provides
            transform_func: Function to transform raw data to entity type
            cache_ttl_seconds: How long to cache data before refreshing (in seconds)
        """
        self.path = normalize_path_for_spark(path)
        self.entity_type = entity_type
        self.transform_func = transform_func
        self.cache_ttl_seconds = cache_ttl_seconds
        self._cache: Optional[List[T]] = None
        self._last_refresh: Optional[float] = None
    
    def get_data(self) -> List[T]:
        """Get data, using cache if available and not expired."""
        current_time = time.time()
        
        # If cache is empty or expired, refresh it
        if (self._cache is None or 
            self._last_refresh is None or 
            current_time - self._last_refresh > self.cache_ttl_seconds):
            self._refresh_cache()
            
        return self._cache or []
    
    def _refresh_cache(self) -> None:
        """Refresh the data cache."""
        try:
            if not check_file_path(self.path):
                logger.error(f"Path not found: {self.path}")
                self._cache = []
                self._last_refresh = time.time()
                return
                
            logger.info(f"Reading CSV files from path: {self.path}")
            df = read_csv_files_to_polars_df(self.path)
            self._cache = []
            for row in df.iter_rows(named=True):
                self._cache.append(self.transform_func(cast(Dict[str, Any], row)))
            
            # records = df.to_dict(orient='records')
            # self._cache = [self.transform_func(cast(Dict[str, Any], row)) for row in records]
            self._last_refresh = time.time()
            logger.info(f"Loaded {len(self._cache)} records for {self.entity_type.__name__}")      
        except Exception as e:
            logger.error(f"Error refreshing {self.entity_type.__name__} data: {str(e)}")
            # Don't clear cache on error - keep old data if we have it
            if self._cache is None:
                self._cache = []
            self._last_refresh = time.time()

    def clear_cache(self) -> None:
        """Force clear the cache."""
        self._cache = None
        self._last_refresh = None