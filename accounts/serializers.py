from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Tags, BlogPost
import time


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('username', 'password')
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



class BlogPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'body', 'author', 'created_at', 'updated_at', 'category', 'tags')
        extra_kwargs = {'author': {'required': False}}

    def create(self, validated_data):
        try:
            author = self.context['request'].user
            try:
                tags = validated_data.pop('tags')
            except:
                tags = []

            blogpost = BlogPost.objects.create(author=author, **validated_data)
            for tag in tags:
                blogpost.tags.add(tag)

            return blogpost
        except:
            raise serializers.ValidationError("Something went wrong")





    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['author'] = instance.author.username
        try:
            response['category'] = Category.objects.filter(id=instance.category.id).values('name','id')
        except:
            response['category'] = None
        response['tags'] = [tag.name for tag in instance.tags.all()]
        response['current_time'] = time.time()
        return response




