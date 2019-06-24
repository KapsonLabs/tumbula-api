import sys
import json
import re

from accounts.models import User
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings
from rest_framework import permissions
from accounts.serializers import TokenSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response 

from .serializers import CreateUserSerializer

# Get the JWT settings, add these lines after the import/from lines
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginView(APIView):
    """
    POST auth/login/
    """
    # This permission class will overide the global permission
    # class setting
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)

            token_serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            token_serializer.is_valid()
            data_dict = {"status":200, "data": {"token":token_serializer.data}}
            return Response(data_dict, status=status.HTTP_200_OK)
        return Response({"status":404, "error":"username or password incorrect"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        public_address = self.request.query_params.get('public_address')
        user_details = User.objects.get(public_address=public_address)

        user = authenticate(request, username=user_details.username, password="hall65536")
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)

            token_serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            token_serializer.is_valid()
            data_dict = {"status":200, "data": {"token":token_serializer.data}}
            return Response(data_dict, status=status.HTTP_200_OK)
        return Response({"status":404, "error":"username or password incorrect"}, status=status.HTTP_404_NOT_FOUND)

    
class RegisterView(generics.CreateAPIView):
    """
    POST auth/register/
    """

    # This permission class will overide the global permission
    # class setting
    permission_classes = (permissions.AllowAny,)

    def post(self,request, *args, **kwargs):

        user_data = request.data.copy()
        role    = user_data.pop('role', None)

        serializer = CreateUserSerializer(data=user_data)
        if serializer.is_valid():
            print(user_data)
            if role[0]=='ADMIN':
                serializer.save(is_administrator=True)
            elif role[0]=='STORE_OWNER':
                serializer.save(is_store_owner=True)

            data_dict = {"status":201, "data":serializer.data}
            return Response(data_dict, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)