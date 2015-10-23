# from django.apps import apps
# from django.db.migrations.autodetector import MigrationAutodetector
# from django.db.migrations.loader import MigrationLoader
# from django.db.migrations.state import ProjectState
# from django.db.migrations.questioner import MigrationQuestioner
# from django.test import TransactionTestCase

# from simple_app.models import SimpleObject


# class MigrationsTests(TransactionTestCase):
#     """
#     Tests that the generic migration generates with swappable dependency
#     """

#     def test_migration_content(self):
#         loader = MigrationLoader(None, ignore_no_migrations=True)
#         questioner = MigrationQuestioner(specified_apps=(), dry_run=False)

#         autodetector = MigrationAutodetector(
#             loader.project_state(),
#             ProjectState.from_apps(apps),
#             questioner
#         )

#         changes = autodetector.changes(
#                 graph=loader.graph,
#                 trim_to_apps=['simple_app'] or None,
#                 convert_apps=['simple_app'] or None,
#                 migration_name=None
#             )

#         import pdb; pdb.set_trace()
