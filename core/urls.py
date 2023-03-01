from django.urls import path
from django.http import HttpRequest

def home(request: HttpRequest):
    data = request.GET
    print(data['a'])
    pass


urlpatterns = [
    path('home/', home),
]
