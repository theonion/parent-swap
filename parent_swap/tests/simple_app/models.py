from django.db import models

from parent_swap.swap import BaseModel


class SimpleObject(BaseModel):
    """
    Basic object inheriting from an abstract base class
    """
    foo = models.CharField(max_length=256)
