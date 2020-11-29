from rest_framework import serializers
from .models import Post


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'description',
            'photo',
            #   'author',
            #   'category',
            #   'is_published',
            #   'authorized_by'
            'created_at',
            'updated_at'
        ]
