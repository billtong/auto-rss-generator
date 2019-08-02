import configparser
import operator

from server.slack_service.main import slack_channel_rss
from server.slack_service.web_driver import SLACK_WEB_DRIVER
from server.yammer_service.main import yammer_group_rss
from server.yammer_service.web_driver import YAMMER_WEB_DRIVER


def multi_yammer_source_combine(yammer_urls):
    yammer_driver = YAMMER_WEB_DRIVER.get_driver()
    list_all = []
    for url in yammer_urls:
        list_all += yammer_group_rss(url, yammer_driver)
    return list_all


def multi_slack_source_combine(slack_urls):
    slack_driver = SLACK_WEB_DRIVER.get_driver()
    list_all = []
    for url in slack_urls:
        list_all += slack_channel_rss(url, slack_driver)
    return list_all


def final_list_combine():
    config = configparser.ConfigParser()
    config.read_file(open("server/urls.ini"))
    slack_urls = config["urls"]["slack"].split(",")
    yammer_urls = config["urls"]["yammer"].split(",")
    slack_list = multi_slack_source_combine(slack_urls)
    yammer_list = multi_yammer_source_combine(yammer_urls)
    final_list = yammer_list + slack_list
    final_list.sort(key=operator.itemgetter('published'), reverse=True)
    return final_list
