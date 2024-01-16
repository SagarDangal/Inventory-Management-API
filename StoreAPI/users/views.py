from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import UserRegistrationSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from drf_yasg.utils import swagger_auto_schema

#viewset for user registration


class UserRegistrationViewSet(viewsets.GenericViewSet):
        queryset = User.objects.all()
        serializer_class = UserRegistrationSerializer

        @swagger_auto_schema(request_body=UserRegistrationSerializer)
        def create(self, request):
            serializer = UserRegistrationSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                if user:
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
