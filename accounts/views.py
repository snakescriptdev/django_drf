from rest_framework import viewsets
from django.shortcuts import render
from accounts.models import Student
from accounts.serializers import StudentSerializer

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


