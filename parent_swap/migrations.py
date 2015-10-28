from .swap import _get_class_object


def get_cls_ptr(cls):
    """
    Returns the name of the class pointer for a given OneToOne relationship.
    """
    if isinstance(cls, str):
        cls = _get_class_object(cls)
    return '{}_ptr'.format(cls._meta.object_name.lower())


def get_swap_field(cls):
    pass
