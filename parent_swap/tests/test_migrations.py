from parent_app import models

from ..migrations import get_cls_ptr
from .utils import AppReloadTestCase


class TestMigrationSwap(AppReloadTestCase):

    def test_get_cls_ptr(self):
        ptr = get_cls_ptr(models.SimpleParent)
        self.assertEquals(ptr, 'simpleparent_ptr')
