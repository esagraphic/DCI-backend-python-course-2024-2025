
class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # Check if an instance of the class already exists
        if cls not in cls._instances:
            # Create and store the new instance if it doesn't exist
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        # Return the existing instance
        return cls._instances[cls]
