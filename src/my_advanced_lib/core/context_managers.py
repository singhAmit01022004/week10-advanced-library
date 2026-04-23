from contextlib import contextmanager


@contextmanager
def file_manager(path: str, mode: str):
    """Context manager for file handling"""
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()