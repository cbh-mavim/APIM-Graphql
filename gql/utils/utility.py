
from pathlib import Path
from gql.config import tables_names

def normalize_path_for_spark(path: str) -> str:
    """
    Normalize a file system path for Spark by converting backslashes to forward slashes.
    
    Args:
        path: The file path to normalize
        
    Returns:
        str: Normalized path with forward slashes
    """
    return path.replace('\\', '/')

def check_file_path(file_path: str) -> bool:
    """
    Check if the provided file path is valid and corresponds to a directory in the specified tables names.
    
    Args:
        file_path (str): The file path to check
        
    Returns:
        bool: True if the file path is valid, False otherwise
    """
    # Ensure the file_path is a directory path
    subfolder_prefix = file_path.split('/')[-1]
    print(f"Subfolder prefix: {subfolder_prefix}")
    if subfolder_prefix in tables_names:
        return True
    else:
        return False