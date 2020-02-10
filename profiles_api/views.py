from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers



class HelloApiView(APIView):
    """Teste Api View"""
    serializer_class = serializers.HelloSerializer

    def get(self, resquest, format=None):
        """ Resturn a list of Apiviews"""
        an_apiview = [
            'Uses Http mehtods as function(get, post,patch, put , delete)'

        ]

        return Response({'message':'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """create a msg with name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def put(self, request, pk=None):
        """Handle updating object"""
        
