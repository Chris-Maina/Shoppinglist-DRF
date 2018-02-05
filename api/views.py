""" api/views.py """

from .models import Shoppinglist, User
from .serializers import ShoppinglistSerializer, UserSerializer
from rest_framework import generics, response, status, views
from rest_framework.decorators import api_view

# Create your views here.
class UserRegisterView(views.APIView):   
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer()
        return response.Response(serializer.data)

    def post(self, request):
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid(raise_exception=True):
            serialized.save()
            return response.Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid(raise_exception=True):
            serialized.save()
            return response.Response(serialized.data, status=status.HTTP_202_ACCEPTED)
        else:
            return response.Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

class ShoppinglistView(generics.ListCreateAPIView):
    """ Defines post and get behaviour of Shoppinglist model """
    queryset = Shoppinglist.objects.all()
    serializer_class = ShoppinglistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)

class ShoppinglistDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ Defines get a single list,put and delete behaviour of Shoppinglist model """
    queryset = Shoppinglist.objects.all()
    serializer_class = ShoppinglistSerializer
        