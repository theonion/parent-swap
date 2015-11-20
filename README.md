# Parent Swap
Swaps the parent class for Django & Django REST Framework.

All of our sites rely on custom base classes and we want to be able to install standalone Django applications with configurable base classes.


# Configuration

To configure the relevant BaseClass for a given object the following parameters must be set in Django settings.

The default base model for the given project.
```
DEFAULT_BASE_MODEL = 'myproject.apps.app.models.MyBaseModel'
```

The default serializer for the default base model.
```
DEFAULT_BASE_SERIALIZER = 'myproject.apps.app.serializers.MyBaseModelSerializer'
```

The default view. 
**the verbage is currently different as it does not inherently relate to the base model.
```
DEFAULT_VIEW = 'myproject.apps.app.views.MyView
```

*IMPORTANT*: Whatever standalone app you use MUST be configured for its migrations to be generated in the project and not ship with pre-built migrations
```
MIGRATION_MODULES = {
  'my_standalone_app': 'myproject.apps.migrations.my_standalone_app_migrations'
```

run
```
python manage.py makemigrations
```
after the application is installed and the settings are configured to create the migration files


# Implementation

## Models & Mapping

The default Mapping is elasticsearch specific and can be ignored if you aren't implementing djes. Otherwise it references the mapping of the 
base model.

```python
from django.db import models

from parent_swap import swap

class SimpleModel(swap.get_base_model()):
  
  foo = models.CharField(max_length=256)
  
  class Mapping(swap.get_base_mapping()):
    pass
    
```

## Serializers

```python
from parent_swap import swap

class SimpleModelSerializer(swap.get_base_serializer()):
  pass
  
```

## Views
```python
from parent_swap import swap

class SimpleModelView(swap.get_base_view()):
    pass

``` 


# Installation

```
pip install parent-swap
```





