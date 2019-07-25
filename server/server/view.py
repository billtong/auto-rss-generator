from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from server.slack_service import slack_channel_rss

@csrf_exempt
def get_rss(request):
    
    '''
    email = request.POST['email']
    password = request.POST['password']
    url = request.POST['url']
    slack_channel_rss(url, email, password, True)
    url = request.GET['url']
    email = ""
    password = ""
    is_headless = True
    slack_channel_rss(url, email, password, is_headless)
    '''
    f = open("server/slack_devops_channel_rss.xml", "r")
    str = f.read()
    
    return HttpResponse(str)