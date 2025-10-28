import logging

def get_logger(name=None,level=logging.WARNING):
    """
    Returns a configured logger instance.
    
    Args:
        name: Optional name for the logger (typically __name__ from the calling module)
    
    Returns:
        Configured logger instance
    """
    logging.basicConfig(
    level=level,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
    )
    logger = logging.getLogger(name)
    
    return logger