import configparser

from server.slack_service.collect import auto_collect_data
from server.slack_service.login import auto_login
from server.slack_service.web_driver import SLACK_WEB_DRIVER
from server.manulife_service.login import url_login


def slack_rss_feed_login():
    driver = SLACK_WEB_DRIVER.get_driver()
    config = configparser.ConfigParser()
    config.read_file(open("server/application.ini"))
    username = config["auth"]["username"]
    email = config["auth"]["email"]
    password = config["auth"]["password"]
    url_login(driver, username, password)
    auto_login(driver, email)


def slack_channel_rss(url_path, driver):
    driver.get(url_path)
    entry_dic_list = auto_collect_data(driver)
    return entry_dic_list
