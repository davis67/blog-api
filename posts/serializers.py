from rest_framework import serializers
from .models import Post


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title',
                  'description',
                  #   'author',
                  #   'category',
                  #   'is_published',
                  #   'authorized_by'
                  ]
