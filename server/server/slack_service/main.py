import configparser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from server.slack_service.collect import auto_collect_data
from server.slack_service.web_driver import SLACK_WEB_DRIVER
from server.manulife_service.login import basic_auth


def slack_rss_feed_login(is_refresh):
    if is_refresh:
        SLACK_WEB_DRIVER.refresh_driver()
    driver = SLACK_WEB_DRIVER.get_driver()
    config = configparser.ConfigParser()
    config.read_file(open("server/application.ini"))
    username = config["auth"]["username"]
    email = config["auth"]["email"]
    password = config["auth"]["password"]
    slack_index_url = config["index_urls"]["slack"]
    basic_auth(driver, username, password)
    print("start slack sign in")
    driver.get(slack_index_url)
    login_btn = driver.find_element_by_id("enterprise_member_guest_account_signin_link")
    login_btn.click()
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "loginfmt"))
    )
    email_input.clear()
    email_input.send_keys(email, Keys.RETURN)
    print("finish slack sign in")


def slack_channel_rss(url_path, driver):
    driver.get(url_path)
    entry_dic_list = auto_collect_data(driver)
    return entry_dic_list
