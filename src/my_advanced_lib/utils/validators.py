from ..exceptions import ValidationError


def validate_positive(value: int):
    """Check if value is positive"""
    if value < 0:
        raise ValidationError("Value must be positive")