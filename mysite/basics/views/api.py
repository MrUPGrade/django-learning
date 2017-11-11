from django.http import JsonResponse
from rest_framework.decorators import api_view


# @csrf_exempt
@api_view(['GET', 'POST'])
def hello_world(request):
    print(request.data)
    return JsonResponse({'message': 'Hello world!'})
