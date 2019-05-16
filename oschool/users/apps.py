from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "oschool.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import oschool.users.signals  # noqa F401
        except ImportError:
            pass
