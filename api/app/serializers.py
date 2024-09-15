from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password')

    def create(self, validated_data):
        print(validated_data)
        user = User(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
