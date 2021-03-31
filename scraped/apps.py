import os

from django.apps import AppConfig

class MainappConfig(AppConfig):
    name = 'scraped'

    def ready(self):
        from . import jobs

        # if os.environ.get('RUN_MAIN', None) != 'true':
        jobs.Command()

class ScrapedConfig(AppConfig):
    name = 'scraped'   

    def ready(self):
        
        from . import jobs

        # if os.environ.get('RUN_MAIN', None) != 'true':
        jobs.Command()