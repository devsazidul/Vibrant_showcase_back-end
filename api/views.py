from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def test_api(request):
    return Response({
        'message': 'Django API is working!',
        'status': 'success'
    })

@api_view(['GET', 'POST'])
def hello(request):
    if request.method == 'GET':
        return Response({
            'message': 'Hello from Django Backend!'
        })
    elif request.method == 'POST':
        name = request.data.get('name', 'Guest')
        return Response({
            'message': f'Hello {name}!'
        })