from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
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
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete object"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """test api viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Retun message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)'
            'automatically maps'
        ]

        return Response({'message':'Hello', 'a_viewset':a_viewset})

    def create(self, resquest):
        """create a new hello """
        serializer = self.serializer_class(data=resquest.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method':'GET'})


    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Destroy remove object"""
        return Response({'http_method':'DELETE'})
