
def get_cls_ptr(cls):
    """
    Returns the name of the class pointer for a given OneToOne relationship.
    """
    return '{}_ptr'.format(cls._meta.object_name.lower())
