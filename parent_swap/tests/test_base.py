from django.test import TestCase

from simple_app.models import SimpleObject


class TestSimpleObject(TestCase):
    """
    Tests swappable base class object models
    """
    def test_no_base_simpleobject(self):
        simple = SimpleObject.objects.create(foo='hey hey hey', bar='yo yo yo')
        simple.save()
        self.assertTrue(SimpleObject.objects.filter(id=simple.id))
