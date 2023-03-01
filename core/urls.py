from django.urls import path
from django.http import HttpRequest, HttpResponse, JsonResponse

def home(request: HttpRequest):
    # get query agruments
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)

    # response data
    response = {
        "result": int(a) + int(b)
    }

    return JsonResponse(response)


urlpatterns = [
    path('home/', home),
]
