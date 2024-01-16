from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

     #check if the user exists
    def validate(self, data):
        user = User.objects.filter(username=data['username']).first()
        if user:
            raise serializers.ValidationError("User already exists")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user