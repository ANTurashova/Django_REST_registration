from django.apps import AppConfig


class ProfilesAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profiles'

    def ready(self):
        from user_profiles import signals
