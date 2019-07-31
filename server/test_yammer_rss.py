import operator

from server.yammer_service.main import yammer_group_login
from server.yammer_service.main import yammer_group_rss
from server.yammer_service.web_driver import YAMMER_WEB_DRIVER

driver = YAMMER_WEB_DRIVER.get_driver()
yammer_group_login()
url = "https://www.yammer.com/manulife.com/#/threads/inGroup?type=in_group&feedId=12449608"
yammer_list = yammer_group_rss(url, driver)
print(yammer_list)
yammer_list.sort(key=operator.itemgetter('published'), reverse=True)
print(yammer_list)
