""" api/serializers.py """
from rest_framework import serializers
from .models import Shoppinglist
from django.contrib.auth import get_user_model

User = get_user_model()

class ShoppinglistSerializer(serializers.ModelSerializer):
    """ Serializer class for Shoppinglist model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        """ Meta class to map serializer's fields with the model fields. """
        model = Shoppinglist
        fields = ('name', 'description', 'owner', 'date_created', 'date_modified')
        read_only_fields = ("date_created", "date_modified")

class UserSerializer(serializers.ModelSerializer):
    """ Serializer class for Custom user model """
    password1 = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'staff', 'active', 'superuser', 'date_joined', \
        'password1', 'password2')
        read_only_fields = ('staff', 'active', 'superuser', 'date_joined')

    def validate(self, data):
        """ Check for password mismatch and any other validateion """
        if data.get('password1') != data.get('password2'):
            raise serializers.ValidationError("Those passwords don't match.")
        return data

    def create(self, validated_data):
        print(validated_data)
        return User.objects.create_user(
            validated_data['email'],
            validated_data['username'])
