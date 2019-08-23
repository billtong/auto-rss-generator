#!/usr/bin/python

import time

from server.rss_service import final_list_combine, auto_generate_xml
from server.slack_service import slack_rss_feed_login
from server.yammer_service import yammer_group_login

max_loop = 11  # run 11times then update credentials
is_refresh = False
while True:
    slack_rss_feed_login(is_refresh)
    yammer_group_login(is_refresh)
    count = 0
    while True:
        final_list = final_list_combine()
        auto_generate_xml(final_list)
        if count > max_loop:
            is_refresh = True
            break
        print("start sleep")
        time.sleep(60 * 15)  # sleep 15 minutes
        print("end sleep")
        count += 1
