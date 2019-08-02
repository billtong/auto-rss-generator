import configparser

from server.slack_service.collect import auto_collect_data
from server.slack_service.login import auto_login
from server.slack_service.web_driver import SLACK_WEB_DRIVER


def slack_rss_feed_login():
    driver = SLACK_WEB_DRIVER.get_driver()
    config = configparser.ConfigParser()
    config.read_file(open("server/application.ini"))
    email = config["auth"]["email"]
    password = config["auth"]["password"]
    url = "https://app.slack.com/client/TBKNBP9UJ/CC6NQTXEZ"
    driver.get(url)
    auto_login(driver, email, password)


def slack_channel_rss(url_path, driver):
    driver.get(url_path)
    entry_dic_list = auto_collect_data(driver)
    return entry_dic_list
