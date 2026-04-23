class MyLibError(Exception):
    """Base exception for the library"""
    pass


class ValidationError(MyLibError):
    """Raised when validation fails"""
    pass