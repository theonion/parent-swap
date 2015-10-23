from django.test import TestCase

from parent_swap import swap
from simple_app import models


class AppReloadTestCase(TestCase):
    """
    Reloads the relevant python modules to test the swappable models in isolation.
    """

    def setUp(self):
        reload(swap)
        reload(models)
        super(AppReloadTestCase, self).setUp()