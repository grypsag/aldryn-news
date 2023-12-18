# -*- coding: utf-8 -*-

from django.urls import re_path

from aldryn_news.feeds import CategoryFeed, LatestEntriesFeed, TagFeed
from aldryn_news.utils import redirect_to_viewname
from aldryn_news.views import ArchiveView, CategoryListView, NewsDetailView, TaggedListView

urlpatterns = [
    re_path(r'^$', ArchiveView.as_view(), name='latest-news'),
    re_path(r'^feed/$', LatestEntriesFeed(), name='latest-news-feed'),
    re_path(r'^tagged/(?P<tag>[-\w]+)/$', TaggedListView.as_view(), name='tagged-news'),
    re_path(r'^tagged/(?P<tag>[-\w]+)/feed/$', TagFeed(), name='tagged-news-feed'),
    re_path(r'^(?P<year>\d{4})/$', ArchiveView.as_view(), name='archive-year'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', ArchiveView.as_view(), name='archive-month'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', redirect_to_viewname,
        {'viewname': 'archive-month', 'keys': ['year', 'month']}),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]*)/$',
        NewsDetailView.as_view(), name='news-detail'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', CategoryListView.as_view(), name='news-category'),
    re_path(r'^(?P<category_slug>[-\w]+)/feed/$', CategoryFeed(), name='news-category-feed'),
    re_path(r'^(?P<category_slug>[-\w]+)/(?P<year>\d{4})/$', redirect_to_viewname,
        {'viewname': 'archive-year', 'keys': ['year']}),
    re_path(r'^(?P<category_slug>[-\w]+)/(?P<year>\d{4})/(?P<month>\d{1,2})/$', redirect_to_viewname,
        {'viewname': 'archive-month', 'keys': ['year', 'month']}),
    re_path(r'^(?P<category_slug>[-\w]+)/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$',
        redirect_to_viewname, {'viewname': 'archive-month', 'keys': ['year', 'month']}),
    re_path(
        r'^(?P<category_slug>[-\w]+)/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]*)/$',
        NewsDetailView.as_view(), name='news-detail'),
]
