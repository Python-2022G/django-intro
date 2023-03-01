from django.urls import path
from django.http import HttpRequest, HttpResponse, JsonResponse

def home(request: HttpRequest):

    return JsonResponse({})


urlpatterns = [
    path('home/', home),
]
