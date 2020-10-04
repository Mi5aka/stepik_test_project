from django.apps import AppConfig as appConfig
from django.utils.translation import gettext_lazy as _


class AppConfig(appConfig):
    name = 'code_training.app'
    verbose_name = _('App')
