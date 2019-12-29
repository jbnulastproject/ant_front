from rest_framework import serializers
from django.contrib.auth.models import Post
from django.contrib.auth import authenticate
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "writer", "date", "body")


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'writer', 'body')
        extra_kwargs = {"password": {"write_only": True}}

        def create(self, validated_data):
            posts = post.objects.create_post(
                validated_data["title"], validated_data["writer"], validated_data["body"])
            return posts


class
