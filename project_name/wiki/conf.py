from __future__ import absolute_import

from django.conf import settings  # noqa
from django.core.exceptions import ImproperlyConfigured
from django.utils import importlib

from appconf import AppConf


def load_path_attr(path):
    i = path.rfind(".")
    module, attr = path[:i], path[i + 1:]
    try:
        mod = importlib.import_module(module)
    except ImportError as e:
        raise ImproperlyConfigured("Error importing {0}: '{1}'".format(module, e))
    try:
        attr = getattr(mod, attr)
    except AttributeError:
        raise ImproperlyConfigured("Module '{0}' does not define a '{1}'".format(module, attr))
    return attr


class WikiAppConf(AppConf):

    IP_ADDRESS_META_FIELD = "HTTP_X_FORWARDED_FOR"
    HOOKSET = "project_name.wiki.hooks.WikiDefaultHookset"
    PARSE = "project_name.wiki.parsers.markdown_parse"

    def configure_hookset(self, value):
        return load_path_attr(value)()

    def configure_parse(self, value):
        return load_path_attr(value)
