from server.slack_service.main import slack_channel_rss
from server.slack_service.login import auto_login
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

def slack_rss_feed():
    webdriver_path = "server/webdriver/geckodriver"
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path=webdriver_path)
    email = "tongzhi@mfcgd.com"
    password = "$$Bill990226"
    url = "https://app.slack.com/client/TBKNBP9UJ/CC6NQTXEZ"
    driver.get(url)
    auto_login(driver, email, password)
    slack_channel_rss(url, driver)
    driver.close()
if __name__ == '__main__':
    slack_rss_feed()