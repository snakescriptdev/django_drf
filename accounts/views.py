from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
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
    swagger_schema = None




class TagsViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    permission_classes = [AllowAny]
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]

    # filter_backends = [DjangoFilterBackend]
    # filterset_class = BlogPostFilter
    # pagination_class = LimitOffsetPagination

@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST','DELETE','PUT','PATCH'])
def blogpost(request,pk=None):
    if request.method == 'GET':
        if pk:
            blogpost = get_object_or_404(BlogPost, pk=pk)
            serializer = BlogPostSerializer(blogpost)
            return Response(serializer.data)
        else:
            blogpost = BlogPost.objects.all()
            serializer = BlogPostSerializer(blogpost, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BlogPostSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        blogpost = get_object_or_404(BlogPost, pk=pk)
        blogpost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        blogpost = get_object_or_404(BlogPost, pk=pk)
        serializer = BlogPostSerializer(blogpost, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        blogpost = get_object_or_404(BlogPost, pk=pk)
        serializer = BlogPostSerializer(blogpost, data=request.data, partial=True,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UserTokenApi(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]

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









