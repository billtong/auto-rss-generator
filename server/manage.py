#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys

from server.slack_service.main import slack_rss_feed_login
from server.yammer_service.main import yammer_group_login


def main():
    slack_rss_feed_login()
    yammer_group_login()
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
