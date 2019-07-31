from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def driver_init():
    webdriver_path = "server/webdriver/geckodriver"
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path=webdriver_path)
    return driver


class SingletonWebDriver(object):
    def __init__(self):
        self.driver = driver_init()

    def get_driver(self):
        return self.driver


SLACK_WEB_DRIVER = SingletonWebDriver()
