from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Tags, BlogPost
import time


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedRelatedField(view_name='user-detail', lookup_field='pk', read_only=True)

    class Meta:
        model = User
        fields = ('username', 'password','url')
        queryset = User.objects.all()



class CategorySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='category-detail', lookup_field='pk')
    class Meta:
        model = Category
        fields = ('name','id', 'url')



class TagsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Tags.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='blogpost-detail', lookup_field='pk')
    author = serializers.ReadOnlyField(source='author.username')



    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'body', 'author', 'created_at', 'updated_at', 'category', 'tags','url')


    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['author'] = instance.author.username
        response['category'] = instance.category.name
        response['tags'] = [tag.name for tag in instance.tags.all()]
        response['current_time'] = time.time()
        return response

