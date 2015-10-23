from django.db import connection
from django.core.management import call_command
from django.test import TestCase

from parent_swap import swap
from simple_app import models


def drop_database(table_name):
    cursor = connection.cursor()
    cursor.execute(
        '''DROP TABLE {};'''.format(table_name)
    )
    cursor.close()


class AppReloadTestCase(TestCase):
    """
    Reloads the relevant python modules to test the swappable models in isolation.
    """
    def setUp(self):
        reload(swap)
        reload(models)
        super(AppReloadTestCase, self).setUp()
        # We're gonna have to re-run migrations since we want to start in a new environment.
        drop_database(models.SimpleObject._meta.db_table)
        call_command('migrate', verbosity=0)
