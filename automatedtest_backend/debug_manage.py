#!/usr/bin/env python
# coding=utf-8
import os
import sys

def pycharm_debug():
    # 1. 配置debug环境变量（pip install -U python-dotenv）
    from dotenv import load_dotenv
    from pathlib import Path  # python3 only
    debug_env = 'debug.env'

    try:
        env_path = Path('.') / debug_env
        load_dotenv(dotenv_path=env_path)
        secret_key = os.environ['SECRET_KEY']
        name = os.environ['DB_NAME']
    except Exception as err:
        print('%s load failed' % debug_env)
    else:
        print('%s is working' % debug_env)

    # 2. 修改db引擎 (pip install pymysql)
    # import pymysql
    # pymysql.install_as_MySQLdb()


if __name__ == "__main__":

    pycharm_debug()  # 调用后可以pycharm中断点调试
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "general.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)