class RegistryMeta(type):
    """Metaclass for registering classes"""
    registry = {}

    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)
        if name != "Base":
            cls.registry[name] = new_cls
        return new_cls