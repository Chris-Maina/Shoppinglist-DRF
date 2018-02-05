""" api/urls.py """

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import ShoppinglistView, ShoppinglistDetailView, UserRegisterView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('shoppinglists/', ShoppinglistView.as_view(), name="create_list"),
    path('shoppinglists/<int:pk>/', ShoppinglistDetailView.as_view(), name="shoppinglist_details")
]
urlpatterns = format_suffix_patterns(urlpatterns)
