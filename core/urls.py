from django.urls import path
from django.http import HttpRequest, HttpResponse

def home(request: HttpRequest):

    html = "<h1>Hello, World!</h1>"
    return HttpResponse(html)


urlpatterns = [
    path('home/', home),
]
