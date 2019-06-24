from rest_framework import serializers
from accounts.models import User

class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)

class CreateUserSerializer(serializers.ModelSerializer):
    """
    This serializer exposes fields to create a user
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id','username', 'first_name', 'last_name', 'email', 'password', 'public_address')

    def create(self, validated_data):
        user = super(CreateUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserDetailSerializer(serializers.ModelSerializer):
    """
    This serializer return user details
    """

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')