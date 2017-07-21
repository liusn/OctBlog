#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os, sys, datetime

def get_env_value(key, default_value=''):
    if sys.version_info < (3, 0):
        return os.environ.get(key, default_value).decode('utf8')
    else:
        return os.environ.get(key, default_value)


OctBlogSettings = {
    'post_types': ('post', 'page'), # deprecated
    'allow_registration': True,
    'allow_su_creation': True,
    'allow_donate': False,
    'auto_role': os.environ.get('auto_role', 'reader').lower(),
    'blog_meta': {
        'name': get_env_value('name', 'Sn Blog'),
        'subtitle': get_env_value('subtitle', 'SnBlog'),
        'description': get_env_value('description', 'SN Blog Description'),
        'wechat_name': get_env_value('wechat_name', 'Sn Blog Wechat Root'),
        'wechat_subtitle': get_env_value('wechat_subtitle', 'Sn Blog Wechat Subtitle'),
        'owner': get_env_value('owner', 'liusn'),
        'keywords': get_env_value('keywords', 'python,django,flask,docker,MongoDB'),
        'google_site_verification': os.environ.get('google_site_verification') or '12345678',
        'baidu_site_verification': os.environ.get('baidu_site_verification') or '87654321',
        'sogou_site_verification': os.environ.get('sogou_site_verification') or '87654321',
    },
    'search_engine_submit_urls':{
        'baidu': os.environ.get('baidu_submit_url')
    },
    'pagination':{
        'per_page': int(os.environ.get('per_page', 5)),
        'admin_per_page': int(os.environ.get('admin_per_page', 10)),
        'archive_per_page': int(os.environ.get('admin_per_page', 20)),
    },
    'blog_comment':{
        'allow_comment': True,
        'comment_type': os.environ.get('comment_type', 'octblog').lower(), # currently, OctBlog only supports duoshuo comment
        'comment_opt':{
            'octblog': 'oct-blog', # shotname of octblog
            'duoshuo': 'oct-blog', # shotname of duoshuo
            }
    },
    'donation': {
        'allow_donate': False,
        'donation_msg': get_env_value('donation_msg', 'You can donate to me if the article makes sense to you'),
        'donation_img_url': '/static/img/donation.png'
    },
    'wechat': {
        'display_wechat': False,
        'wechat_msg': get_env_value('wechat_msg', 'Welcome to follow my wechat'),
        'wechat_image_url': os.environ.get('wechat_image_url') or 'http://7tsygu.com1.z0.glb.clouddn.com/gevin-view.jpg?imageView/2/w/150',
        'wechat_title': get_env_value('wechat_title', 'GevinView'),
    },
    'copyright': {
        'display_copyright': False,
        'copyright_msg': get_env_value('copyright_msg', 'The article is not allowed to repost unless author authorized')
    },
    'only_abstract_in_feed': os.environ.get('only_abstract_in_feed', 'false').lower() == 'true',
    'allow_share_article': False,
    'gavatar_cdn_base': os.environ.get('gavatar_cdn_base', '//cdn.v2ex.com/gravatar/'),
    'gavatar_default_image': os.environ.get('gavatar_default_image', '/static/img/user-avatar.jpg'),
    'background_image': {
        'home': os.environ.get('bg_home') or '/static/img/bg1.png',
        'post': os.environ.get('bg_post') or '/static/img/bg1.png',
        'about': os.environ.get('bg_about') or '/static/img/bg1.png',
        'qiniu': os.environ.get('qiniu') or '/static/img/bg1.png',
    },
    'daovoice':{
        'allow_daovoice': False,
        'app_id': os.environ.get('daovoice_app_id'),
    }

}

class Config(object):
    DEBUG = False
    TESTING = False

    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fjdljLJDL08_80jflKzcz545135nv*c'
    MONGODB_SETTINGS = {'DB': 'OctBlog'}

    TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates').replace('\\', '/')
    STATIC_PATH = os.path.join(BASE_DIR, 'static').replace('\\', '/')
    EXPORT_PATH = os.path.join(BASE_DIR, 'exports').replace('\\', '/')

    if not os.path.exists(EXPORT_PATH):
        os.makedirs(EXPORT_PATH)

    REMEMBER_COOKIE_DURATION = datetime.timedelta(hours=3)


    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG = False

class PrdConfig(Config):
    # DEBUG = False
    DEBUG = False
    MONGODB_SETTINGS = {
            'db': os.environ.get('DB_NAME') or 'OctBlog',
            'host': os.environ.get('MONGO_HOST') or 'localhost',
            # 'port': 12345
        }

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    MONGODB_SETTINGS = {'DB': 'OctBlogTest'}
    WTF_CSRF_ENABLED = False

config = {
    'dev': DevConfig,
    'prd': PrdConfig,
    'testing': TestingConfig,
    'default': DevConfig,
}
