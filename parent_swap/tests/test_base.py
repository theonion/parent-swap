from django.test import TestCase, override_settings

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


class TestSimpleObject(AppReloadTestCase):
    """
    Tests swappable BaseClass unconfigured: django.db.models.Model
    """
    def test_base(self):
        bases = models.SimpleObject.__bases__
        self.assertEqual(len(bases), 1)
        base_model = bases[0]
        self.assertEqual(base_model.__name__, 'Model')

    def test_create(self):
        simple = models.SimpleObject.objects.create(foo='hey hey hey')
        simple.save()
        self.assertTrue(models.SimpleObject.objects.filter(id=simple.id))


@override_settings(DEFAULT_BASE_CLASS='parent_swap.tests.simple_app.parent_models.SimpleParent')
class TestConfiguredBaseClass(AppReloadTestCase):
    """
    Tests swappable BaseClass configured: SimpleParent
    """
    def test_base(self):
        bases = models.SimpleObject.__bases__
        self.assertEqual(len(bases), 1)
        base_model = bases[0]
        self.assertEqual(base_model.__name__, 'SimpleParent')
