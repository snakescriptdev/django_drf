from rest_framework import serializers

from accounts.models import Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    standard = serializers.IntegerField()
    passout = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

