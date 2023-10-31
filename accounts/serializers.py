from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.models import Student

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class StudentSerializer(serializers.ModelSerializer):
    teacher = UserSerializer(read_only=True)
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'standard', 'city', 'passout', 'teacher']


    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def validate(self, attrs):
        if attrs['roll'] > 100:
            raise serializers.ValidationError('Roll number must be less than 100')
        return attrs

    def validate_name(self, value):
        if len(value) < 4:
            raise serializers.ValidationError('Name must be greater than 4 characters')
        return value



