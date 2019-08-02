import configparser

from server.yammer_service.collect import auto_collect_data
from server.yammer_service.login import auto_login
from server.yammer_service.web_driver import YAMMER_WEB_DRIVER


def yammer_group_login():
    driver = YAMMER_WEB_DRIVER.get_driver()
    url = "https://www.yammer.com/manulife.com/#/threads/inGroup?type=in_group&feedId=12449608"
    driver.get(url)
    config = configparser.ConfigParser()
    config.read_file(open("server/application.ini"))
    email = config["auth"]["email"]
    password = config["auth"]["password"]
    driver.get(url)
    auto_login(driver, email, password)


def yammer_group_rss(url, driver):
    driver.get(url)
    entry_dic_list = auto_collect_data(driver)
    return entry_dic_list
