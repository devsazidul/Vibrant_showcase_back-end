from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def testapi_2(requst):
    return Response({"Success_1: I'm Sazidul islam","Designation: Mobile apps developer"})

    

