from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Student
from accounts.serializers import StudentSerializer

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request, *args, **kwargs):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(queryset)
        return Response(serializer.data)



class StudentAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()  #queryset
        serializer = StudentSerializer(students, many=True) #many=True for queryset and serialization
        return Response(serializer.data)


    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)





