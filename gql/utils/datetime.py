from datetime import datetime
import pytz
import strawberry
from dateutil import parser
# Custom scalar for datetimeoffset
@strawberry.scalar
class DateTimeISO:

    @staticmethod
    def serialize(value) -> str | None:
        """Serialize datetime values to ISO format compatible with Power BI and other consumers."""
        return normalize_datetime_format(value)


def parse_mavim_date(date_str: str) -> str | None:
    """
    Parse a date string and convert it to Europe/Amsterdam timezone.
    Returns None if the input is None or empty string.
    
    Args:
        date_str: The date string to parse
        
    Returns:
        ISO formatted string of timezone-aware datetime or None if input is invalid
    """
    if not date_str or date_str.strip() == '':
        return None
    
    try:
        return parser.parse(date_str).astimezone(pytz.timezone("Europe/Amsterdam")).isoformat()
    except (ValueError, TypeError):
        return None


def normalize_datetime_format(value) -> str | None:
    """
    Normalize various datetime formats to a consistent ISO format.
    Handles formats like:
    - "2020-01-28 09:47:43.0000000 +00:00"
    - "2020-01-28T09:47:43.000Z"
    - Standard ISO formats
    
    Args:
        value: The datetime value to normalize (string, datetime, or None)
        
    Returns:
        ISO formatted string compatible with Power BI or None if invalid
    """
    if value is None:
        return None
    
    if isinstance(value, str):
        value = value.strip()
        if not value:
            return None
            
        try:
            # Handle the specific problematic format: "2020-01-28 09:47:43.0000000 +00:00"
            if '.0000000' in value:
                # Remove excessive precision that causes parsing issues
                value = value.replace('.0000000', '.000')
            
            # Parse the datetime string
            if '+' in value or value.endswith('Z'):
                # It's already timezone-aware
                parsed_date = parser.parse(value)
            else:
                # Assume UTC if no timezone info
                parsed_date = parser.parse(value).replace(tzinfo=pytz.UTC)
            
            # Return in standard ISO format: YYYY-MM-DDTHH:MM:SS.sssZ
            return parsed_date.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z' if parsed_date.tzinfo == pytz.UTC else parsed_date.isoformat()
            
        except (ValueError, TypeError) as e:
            print(f"Warning: Could not parse datetime '{value}': {e}")
            return None
    
    elif isinstance(value, datetime):
        # If it's a datetime object, ensure it has timezone info
        if value.tzinfo is None:
            value = value.replace(tzinfo=pytz.UTC)
        return value.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z' if value.tzinfo == pytz.UTC else value.isoformat()
    
    return None 