from .swap import BaseClass

from .utils import get_applied_migrations


def dependency_exists(dependency):
    """
    validates that the provided dependency is legitimate.
    """
    applied_migrations = get_applied_migrations()
    return bool(dependency in applied_migrations)


def get_model_dependency(cls):
    """
    Retrieves the South Migration dependency for a given Model
    """
    initial_migration = '0001_initial.py'
    dependency = (cls._meta.app_label, initial_migration)
    if not dependency_exists(dependency):
        raise KeyError(
            "The dependency '{0}' does not exist for app '{1}'".format(
                cls._meta.app_label, initial_migration
            )
        )
    return dependency


def get_default_dependency():
    return get_model_dependency(BaseClass)
