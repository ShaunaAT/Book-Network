from django.apps import AppConfig


class GroupsConfig(AppConfig):
    name = 'Groups'
    
    def ready(self):
        import Groups.signals
