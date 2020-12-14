import configparser

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from server.login_service.login import basic_auth
from server.yammer_service.collect import auto_collect_data
from server.webdriver.web_driver import YAMMER_WEB_DRIVER
from server.webdriver.web_driver import WEB_DRIVER_WAIT_TTL


def yammer_group_login(is_refresh):
    if is_refresh:
        YAMMER_WEB_DRIVER.refresh_driver()
    driver = YAMMER_WEB_DRIVER.get_driver()
    config = configparser.ConfigParser()
    config.read_file(open("server/application.ini"))
    yammer_index_url = config["index_urls"]["yammer"]
    username = config["auth"]["username"]
    password = config["auth"]["password"]
    email = config["auth"]["email"]
    basic_auth(driver, username, password)
    driver.get(yammer_index_url)
    print("start yammer sign in")
    email_input = WebDriverWait(driver, WEB_DRIVER_WAIT_TTL).until(
        EC.presence_of_element_located((By.NAME, "loginfmt"))
    )
    email_input.clear()
    email_input.send_keys(email, Keys.RETURN)
    print("finish yammer signin")


def yammer_group_rss(url, driver):
    driver.get(url)
    entry_dic_list = auto_collect_data(driver)
    return entry_dic_list
