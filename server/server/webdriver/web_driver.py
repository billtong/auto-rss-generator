import configparser
from selenium import webdriver

# linux chrome driver is quite slow, so I need 1 min.
WEB_DRIVER_WAIT_TTL = 60


def driver_init():
    # config = configparser.ConfigParser()
    # config.read_file(open("server/application.ini"))
    # selenium_url = config['selenium']['url']
    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # cap = options.to_capabilities()
    # driver = webdriver.Remote(
    #     command_executor=selenium_url,
    #     desired_capabilities=cap
    # )
    webdriver_path = "server/webdriver/chromedriver"
    # options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=webdriver_path);
    return driver


class SingletonWebDriver(object):
    def __init__(self):
        self.driver = driver_init()

    def get_driver(self):
        return self.driver

    def refresh_driver(self):
        self.driver.close()
        self.driver = driver_init()


SLACK_WEB_DRIVER = SingletonWebDriver()
YAMMER_WEB_DRIVER = SingletonWebDriver()

# def fire_fox_driver_init():
#     webdriver_path = "server/webdriver/geckodriver"
#     profile = FirefoxProfile()
#     profile.assume_untrusted_cert_issuer = True
#     profile.accept_untrusted_certs = True
#     capabilities = DesiredCapabilities.FIREFOX.copy()
#     capabilities['acceptInsecureCerts'] = True
#     capabilities['acceptSslCerts'] = True
#     options = Options()
#     options.headless = False
#     ff_binary = FirefoxBinary("/Applications/Firefox Nightly.app/Contents/MacOS/firefox-bin")
#     driver = webdriver.Firefox(options=options, executable_path=webdriver_path, firefox_binary=ff_binary, capabilities=capabilities, firefox_profile=profile)

