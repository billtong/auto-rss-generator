from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from server.rss_service.main import *
from server.rss_service.xml_builder import auto_generate_xml


@csrf_exempt
def get_rss(request):
    f = open("server/final_rss.xml", "r")
    resp = HttpResponse(f.read())
    resp["content-type"] = "text/xml"
    return resp
