from server.rss_service import final_list_combine, auto_generate_xml
from server.slack_service import slack_rss_feed_login
from server.yammer_service import yammer_group_login

slack_rss_feed_login()
yammer_group_login()

while True:
    final_list = final_list_combine()
    auto_generate_xml(final_list)
