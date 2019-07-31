#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from selenium.webdriver.firefox.options import Options
from selenium import webdriver

from server.slack_service.main import slack_channel_rss
from server.slack_service.main import slack_rss_feed_login
from server.slack_service.login import auto_login

import os
import sys
import threading
import time

def main():
    slack_rss_feed_login()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
