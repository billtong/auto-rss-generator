import configparser

from server.yammer_service.collect import auto_collect_data
from server.yammer_service.web_driver import YAMMER_WEB_DRIVER
from server.manulife_service.login import url_login
from server.yammer_service.login import auto_login


def yammer_group_login():
    driver = YAMMER_WEB_DRIVER.get_driver()
    config = configparser.ConfigParser()
    config.read_file(open("server/application.ini"))
    username = config["auth"]["username"]
    password = config["auth"]["password"]
    email = config["auth"]["email"]
    url_login(driver, username, password)
    driver.get("https://www.yammer.com/manulife.com")
    auto_login(driver, email)


def yammer_group_rss(url, driver):
    driver.get(url)
    entry_dic_list = auto_collect_data(driver)
    return entry_dic_list
