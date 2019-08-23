from selenium import webdriver


def driver_init():
    # webdriver_path = "server/webdriver/geckodriver"
    # profile = FirefoxProfile()
    # profile.assume_untrusted_cert_issuer = True
    # profile.accept_untrusted_certs = True
    # capabilities = DesiredCapabilities.FIREFOX.copy()
    # capabilities['acceptInsecureCerts'] = True
    # capabilities['acceptSslCerts'] = True
    # options = Options()
    # options.headless = False
    # ff_binary = FirefoxBinary("/Applications/Firefox Nightly.app/Contents/MacOS/firefox-bin")
    # driver = webdriver.Firefox(options=options, executable_path=webdriver_path, firefox_binary=ff_binary, capabilities=capabilities, firefox_profile=profile)

    webdriver_path = "server/webdriver/chromedriver"
    # options = Options()
    # options.add_argument("--headless")
    # driver = webdriver.Chrome(chrome_options=options, executable_path=webdriver_path);
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
