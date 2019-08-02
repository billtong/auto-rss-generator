import operator

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from server.rss_service.xml_builder import auto_generate_xml
from server.rss_service.main import *
import configparser


@csrf_exempt
def get_rss(request):
    final_list = final_list_combine()
    auto_generate_xml(final_list)
    f = open("server/final_rss.xml", "r")
    resp = HttpResponse(f.read())
    resp["content-type"] = "text/xml"
    return resp

