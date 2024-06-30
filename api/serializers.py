# accounts/serializers.py

from rest_framework import serializers
from .models import CustomUser,Student,ClassName


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']

class ClassSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = ClassName
        fields = ['id', 'className','student']
