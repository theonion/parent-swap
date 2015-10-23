from django.conf import settings


def _get_class_object(path):
    """
    Returns the class instance of the app
    """
    module_name, sp, cls_name = path.rpartition('.')
    mod = __import__(module_name, fromlist=[cls_name])
    return getattr(mod, cls_name)


def _get_default_base_class():
    """
    Returns the class reference in settings.DEFAULT_BASE_CLASS
    """
    base_cls_path = getattr(settings, 'DEFAULT_BASE_CLASS', 'django.db.models.Model')
    return _get_class_object(base_cls_path)


"""Our sweet sweet BaseClass."""
BaseClass = _get_default_base_class()
