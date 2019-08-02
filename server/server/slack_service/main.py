from server.slack_service.collect import auto_collect_data
from server.slack_service.login import auto_login
from server.slack_service.web_driver import SLACK_WEB_DRIVER


def slack_rss_feed_login():
    driver = SLACK_WEB_DRIVER.get_driver()
    email = "tongzhi@mfcgd.com"
    password = "$$Bill990226"
    url = "https://app.slack.com/client/TBKNBP9UJ/CC6NQTXEZ"
    driver.get(url)
    auto_login(driver, email, password)


def slack_channel_rss(url_path, driver):
    driver.get(url_path)
    entry_dic_list = auto_collect_data(driver)
    return entry_dic_list
