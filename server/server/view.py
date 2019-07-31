import operator

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from server.rss_service.xml_builder import auto_generate_xml
from server.slack_service.main import slack_channel_rss
from server.slack_service.web_driver import SLACK_WEB_DRIVER
from server.yammer_service.main import yammer_group_rss
from server.yammer_service.web_driver import YAMMER_WEB_DRIVER


@csrf_exempt
def get_rss(request):
    slack_driver = SLACK_WEB_DRIVER.get_driver()
    yammer_driver = YAMMER_WEB_DRIVER.get_driver()
    yammer_url1 = "https://www.yammer.com/manulife.com/#/threads/inGroup?type=in_group&feedId=12449608"
    slack_url1 = "https://app.slack.com/client/TBKNBP9UJ/CC6NQTXEZ"
    list1 = slack_channel_rss(slack_url1, slack_driver)
    list2 = yammer_group_rss(yammer_url1, yammer_driver)

    final_list = list1 + list2
    final_list.sort(key=operator.itemgetter('published'), reverse=True)
    auto_generate_xml(final_list)
    f = open("server/final_rss.xml", "r")
    resp = HttpResponse(f.read())
    resp["content-type"] = "text/xml"
    return resp
