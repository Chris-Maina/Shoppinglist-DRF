""" api/views.py """

from .models import Shoppinglist
from .serializers import ShoppinglistSerializer
from rest_framework import generics, response


# Create your views here.
class ShoppinglistView(generics.ListCreateAPIView):
    """ Defines post and get behaviour of Shoppinglist model """
    queryset = Shoppinglist.objects.all()
    serializer_class = ShoppinglistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class ShoppinglistDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ Defines get a single list,put and delete behaviour of Shoppinglist model """
    queryset = Shoppinglist.objects.all()
    serializer_class = ShoppinglistSerializer
        