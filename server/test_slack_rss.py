from server.slack_service.login import auto_login
from server.slack_service.main import slack_channel_rss
from server.slack_service.web_driver import SLACK_WEB_DRIVER


def slack_rss_feed():
    driver = SLACK_WEB_DRIVER.get_driver()
    email = "tongzhi@mfcgd.com"
    password = "$$Bill990226"
    url = "https://app.slack.com/client/TBKNBP9UJ/CC6NQTXEZ"
    driver.get(url)
    auto_login(driver, email, password)
    slack_channel_rss(url, driver)
    driver.close()


if __name__ == '__main__':
    slack_rss_feed()
