from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from xml.etree import ElementTree
import time

from server.slack_service.login import auto_login
from server.slack_service.collect import auto_collect_data
from server.slack_service.xml_builder import auto_generate_xml

def slack_channel_rss(url_path, email, password, is_headless):
    webdriver_path = "server/webdriver/geckodriver"
    channel_str = url_path.split("/")[5]
    archive_url_path = "https://mjh-cdn-technology.slack.com/archives/" + channel_str + "/"
    entry_dic_list = []

    options = Options()
    options.headless = is_headless
    driver = webdriver.Firefox(options=options, executable_path=webdriver_path)
    
    driver.get(url_path)
    auto_login(driver, email, password)
    driver.get(url_path)
    entry_dic_list = auto_collect_data(driver, archive_url_path)
    auto_generate_xml(entry_dic_list)
    driver.close()

