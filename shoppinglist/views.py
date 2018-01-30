""" shoppinglist/views.py"""
from rest_framework import generics, response,reverse
from rest_framework.decorators import api_view

# Function based view to return an object with url to api
@api_view(['GET'])
def api_root(request, format=None):
    return response.Response({
        'shoppinglist': reverse.reverse('api:create_list', request=request, format=format),
    })
