"""
Auto collect url patterns from apps.
"""
import os
from tornado.util import import_object
from .settings import BASE_DIR


patterns = []

for app_name in os.walk(os.path.join(BASE_DIR, 'apps')).next()[1]:
    try:
        app_url_patterns = import_object(
            'service.apps.{0}.urls.patterns'.format(app_name))
        patterns += app_url_patterns
    except ImportError:
        pass
