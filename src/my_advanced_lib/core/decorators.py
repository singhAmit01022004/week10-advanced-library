from functools import wraps
import time
from typing import Callable, Any


def retry(attempts: int = 3, delay: float = 1.0) -> Callable:
    """Retry decorator"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for i in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if i == attempts - 1:
                        raise
                    time.sleep(delay)

        return wrapper

    return decorator