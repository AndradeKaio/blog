#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'Kaio Henrique'
SITENAME = 'Kaio Henrique'
SITEURL = 'blog'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'


THEME = 'output/theme/flasky/'

#ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
#ARTICLE_SAVE_AS = ARTICLE_URL

ARTICLE_PATHS = ['blog']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social

SECTIONS = [
        ('Blog', 'index.html'),
        ('Random', 'archives.html'),
        ('Research', 'tags.html'),
        ('About', 'pages/about-me.html')]

DEFAULT_PAGINATION = 10



# =============================
DISQUS_SITENAME = "kaiohenrique-me"
TWITTER_USERNAME = 'eunaokaio'
GITHUB_URL = 'http://github.com/AndradeKaio'
MAIL_USERNAME = 'kaiohenrique'
MAIL_HOST = 'protonmail.com'

# Optional analytic trackers
# =============================
#GOOGLE_ANALYTICS_ACCOUNT = 'UA-00000000-1'
#PIWIK_URL = 'myurl.com/piwik'
#PIWIK_SSL_URL = 'myurl.com/piwik'
#PIWIK_SITE_ID = '1'




# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
