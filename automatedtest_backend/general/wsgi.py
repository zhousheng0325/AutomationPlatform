"""
WSGI config for automatedtest_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application



def pycharm_debug():
    # 1. 配置debug环境变量（pip install -U python-dotenv）
    from dotenv import load_dotenv
    from pathlib import Path  # python3 only
    debug_env = 'debug.env'

    try:
        env_path = Path('.')  / debug_env
        print("-------------------------hahahhah---------------")
        load_dotenv(dotenv_path=env_path)
        secret_key = os.environ['SECRET_KEY']

        print("-------------------",secret_key,"----------------")
        name = os.environ['DB_NAME']
        print("--------",name,"-------------------------")

    except Exception as err:
        print('%s load failed' % debug_env)
    else:
        print('%s is working' % debug_env)

    # 2. 修改db引擎 (pip install pymysql)
    # import pymysql
    # pymysql.install_as_MySQLdb()


pycharm_debug()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'general.settings')
application = get_wsgi_application()
