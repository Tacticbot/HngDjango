from django.shortcuts import render 
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
import datetime

def index(request):
    return HttpResponse("Hello, world. You're at the task1 index. i am Musa and i am Great")

def api(request): 
    slack_name = request.GET.get('slack_name')
    utc_time = timezone.now()
    utc = utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    current_day = utc_time.strftime('%A')
    track = request.GET.get('track')
    data = {
        'slack_name': slack_name,
        "current_day": current_day,
        "utc_time": utc,
        'track': track,
        "github_file_url": "https://github.com/Tacticbot/HngTask1/blob/main/main/views.py",
        "github_repo_url": "https://github.com/Tacticbot/HngTask1",
        "status_code": 200

    }
    return JsonResponse(data)



def musa(request):
    return HttpResponse("Hi this Musa route")