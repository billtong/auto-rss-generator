from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_rss(request):
    f = open("server/final_rss.xml", "r")
    resp = HttpResponse(f.read())
    resp["content-type"] = "text/xml"
    return resp
