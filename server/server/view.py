from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from server.slack_service.main import slack_channel_rss
from server.slack_service.web_driver import SLACK_WEB_DRIVER

@csrf_exempt
def get_rss(request):
    driver = SLACK_WEB_DRIVER.get_driver()
    url = request.GET['url']
    slack_channel_rss(url, driver)
    f = open("server/slack_devops_channel_rss.xml", "r")
    str = f.read()
    resp = HttpResponse(str)
    resp["content-type"] = "text/xml"
    return resp