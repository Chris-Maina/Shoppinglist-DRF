""" api/serializers.py """
from rest_framework import serializers
from .models import Shoppinglist

class ShoppinglistSerializer(serializers.ModelSerializer):
    """ Serializer class for Shoppinglist model instance into JSON format."""
    class Meta:
        """ Meta class to map serializer's fields with the model fields. """
        model = Shoppinglist
        fields = ('name', 'description', 'date_created', 'date_modified')
