from django.db import models

from .swap import _get_class_object


def get_cls_ptr(cls):
    """
    Returns the name of the class pointer for a given OneToOne relationship.
    """
    if isinstance(cls, str):
        cls = _get_class_object(cls)
    return '{}_ptr'.format(cls._meta.object_name.lower())


def get_app_reference(cls):
    """
    Return simplified App Model reference e.g., app_label.ModelName
    """
    return '{0}.{1}'.format(cls._meta.app_label, cls._meta.object_name)


def get_one_to_one_field_config(cls):
    """
    Returns the models.OneToOneField necessary for the migration file.
    Parent Class specific currently.
    """
    if isinstance(cls, str):
        cls = _get_class_object(cls)
    app_reference = get_app_reference(cls)
    return models.OneToOneField(
        parent_link=True, auto_created=True, primary_key=True, serialize=False, to=app_reference
    )


def get_swap_field(cls):
    """
    Returns the appropriately configured field for a swapped model in a migration
    """
    ptr = get_cls_ptr(cls)
    return (ptr,)
