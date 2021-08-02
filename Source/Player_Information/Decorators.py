from Source.Player_Information.ClassFeature import ClassFeature


def feature(name: str, level: int = 1, cls=ClassFeature):
    def wrapper(func):
        func.is_feature = True
        func.name, func.level, func.feature_class = name, level, cls
        return func

    return wrapper


def playable(cls):
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        for name, attr in cls.__dict__.items():
            if hasattr(attr, "is_feature"):
                _cls = attr.feature_class
                setattr(instance, name, _cls(instance, attr, attr.name, attr.level))
        return instance

    return wrapper
