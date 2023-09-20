# -*- coding: utf-8 -*-
from aldryn_apphooks_config.admin import BaseAppHookConfig
from aldryn_apphooks_config.app_base import CMSConfigApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import gettext_lazy as _

from aldryn_news.cms_appconfig import NewsConfig
from aldryn_news.cms_menus import NewsCategoryMenu


class NewsApp(CMSConfigApp):
    name = _('News')
    app_config = NewsConfig

    def get_urls(self, page=None, language=None, **kwargs):
        return ['aldryn_news.urls']

    def get_menus(self, page=None, language=None, **kwargs):
        return [NewsCategoryMenu]


apphook_pool.register(NewsApp)
