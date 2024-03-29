from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .validate_serializers import *


class UserAuthorizationAPIView(APIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK,
                        data={'example forms': {
                            'username': 'John',
                            'password': '12345678'
                        }})

    def post(self, request):
        serializer = UserValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED,
                        data={'error': 'User not found or password is bad!'})


class UserRegistrationAPIView(APIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK,
                        data={'example forms': {
                            'username': 'John',
                            'password': '12345678'
                        }})

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)
