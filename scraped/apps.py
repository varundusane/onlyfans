import os

from django.apps import AppConfig

# class MainappConfig(AppConfig):
#     name = 'core'
#
#     def ready(self):
#         from . import jobs
#
#         # if os.environ.get('RUN_MAIN', None) != 'true':
#         jobs.start_scheduler()

class ScrapedConfig(AppConfig):
    name = 'scraped'
    run_already = False

    def ready(self):
        ScrapedConfig.run_already = True
        print("app")
        from . import jobs

        if os.environ.get('RUN_MAIN', None) != 'true':
            jobs.start_scheduler()