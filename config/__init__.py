# -*- coding: utf-8 -*-
from __future__ import absolute_import

__all__ = ['celery_app', 'RUN_VER', 'APP_CODE', 'SECRET_KEY', 'BK_URL', 'BASE_DIR']

import os

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from blueapps.core.celery import celery_app

# app 基本信息

# SaaS运行版本，如非必要请勿修改
RUN_VER = 'open'
# SaaS应用ID
APP_CODE = 'whisky001'
# SaaS安全密钥，注意请勿泄露该密钥
# SECRET_KEY = '71c0c406-7037-4c98-ad33-865306573458' # 腾讯云环境秘钥
SECRET_KEY = '73e07020-c770-4fc0-99cf-6eea9f759c84'  # 本地秘钥
# 蓝鲸SaaS平台URL, 如 https://paas.blueking.com/
# BK_URL = 'http://paas.class.o.qcloud.com:8000'
BK_URL = 'http://paas.class.o.qcloud.com:80'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(
    __file__)))
