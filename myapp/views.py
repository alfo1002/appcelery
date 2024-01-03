import time
from django.shortcuts import render
from django.http import JsonResponse

from myapp.tasks import waitNSeconds

# ok
#def slowResponseView(request):
#   time.sleep(10)
#    return JsonResponse({"response": "ok"})

def slowResponseView(request):
    waitNSeconds.delay(3)
    return JsonResponse({"response": "ok"})