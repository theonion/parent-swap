from django.test import TestCase

from simple_app.models import SimpleObject


class TestSimpleObject(TestCase):
    """
    Tests swappable base class object models
    """
    def test_base_no_base_simpleobject(self):
        bases = SimpleObject.__bases__
        self.assertEqual(len(bases), 1)
        base_model = bases[0]
        self.assertEqual(base_model.__name__, 'Model')

    def test_create_no_base_simpleobject(self):
        simple = SimpleObject.objects.create(foo='hey hey hey')
        simple.save()
        self.assertTrue(SimpleObject.objects.filter(id=simple.id))
