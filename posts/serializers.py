from rest_framework import serializers
from .models import Post
from authentication.models import User
from authentication import serializers as user_serializers


class PostsSerializer(serializers.ModelSerializer):

    author = user_serializers.UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'description',
            'photo',
            'author',
            #   'category',
            'is_published',
            'authorized_by',
            'created_at',
            'updated_at'
        ]

        read_only_fields = ["author", "authorized_by"]
