from django.urls import path
from django.http import HttpRequest

def home(request: HttpRequest):
    print(request.method)
    print(request.path)
    print(request.content_type)
    pass


urlpatterns = [
    path('home/', home),
]
