from selenium.webdriver.firefox.options import Options
from selenium import webdriver

def driver_init():
    webdriver_path = "server/webdriver/geckodriver"
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path=webdriver_path)
    return driver

class Singleteon_Slack_Webdriver(object):
    def __init__(self):
        self.driver = driver_init()
    def get_driver(self):
        return self.driver

SLACK_WEB_DRIVER = Singleteon_Slack_Webdriver()
