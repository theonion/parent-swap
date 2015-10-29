from parent_swap.dependencies import get_model_dependency
from parent_swap.tests.parent_app.models import SimpleParent

from .utils import AppReloadTestCase


class TestModelDependencies(AppReloadTestCase):

    def test_get_model_dependency(self):
        dependency = get_model_dependency(SimpleParent)
        self.assertEqual(dependency[0], 'parent_app')
        self.assertEqual(dependency[1], '0001_initial.py')
