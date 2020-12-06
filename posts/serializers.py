from rest_framework import serializers
from .models import Comment, Post
from authentication.models import User
from authentication import serializers as user_serializers


class CommentSerializer(serializers.ModelSerializer):
    author = user_serializers.UserSerializer(read_only=True)
    # post = PostsSerializer(read_only=True)

    class Meta:
        model = Comment

        fields = [
            'id',
            'description',
            'author',
            'post',
            'created_at',
            'updated_at'
        ]

        read_only_fields = ["author", 'post']


class PostsSerializer(serializers.ModelSerializer):

    author = user_serializers.UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)


    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'description',
            'photo',
            'author',
            'comments',
            #   'category',
            'is_published',
            'authorized_by',
            'created_at',
            'updated_at'
        ]

        read_only_fields = ["author", 'comments' "authorized_by"]



