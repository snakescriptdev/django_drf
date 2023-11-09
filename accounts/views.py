from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import BlogPostFilter
from .models import Category, Tags, BlogPost
from .serializers import CategorySerializer, TagsSerializer, BlogPostSerializer, UserSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagsViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    permission_classes = [AllowAny]
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = BlogPostFilter
    # pagination_class = LimitOffsetPagination



class UserTokenApi(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

    def post(self, request):
        try:
            username = request.data['username']
            password = request.data['password']
        except:
            return Response({'error': 'Please provide both username and password'})
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid Credentials'})






    # def post(self, request):
    #
    #     user = User.objects.get(id=request.user.id)
    #     token, created = Token.objects.get_or_create(user=user)
    #     return Response({'token': token.key})









