from django.http import HttpRequest, HttpResponse, JsonResponse
import json

def home(request: HttpRequest):
    # get query agruments
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)

    # response data
    response = {
        "result": int(a) + int(b)
    }

    return JsonResponse(response)


def get_sum(request: HttpRequest) -> JsonResponse:
    """
    get the sum of two numbers 

    Args:
        request (HttpRequest): request object
    
    Returns:
        JsonResponse: response object like {"result": 10}
    """
    if request.method == 'GET':
        return HttpResponse("ok")
    
    if request.method == 'POST':
        body = request.body.decode()  # get post request data as string
        data = json.loads(body)  # str to dict

        return JsonResponse({
            "result": data['a'] + data['b']
        })
