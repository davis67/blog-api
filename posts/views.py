from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework import permissions
from .serializers import PostsSerializer
from .permissions import IsOwner
from .models import Post


class ImageUploadParser(FileUploadParser):
    media_type = 'image/*'


class PostCreateAPIView(CreateAPIView):

    serializer_class = PostsSerializer

    parser_class = (ImageUploadParser,)

    # permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save()


class PostListAPIView(ListAPIView):
    serializer_class = PostsSerializer
    queryset = Post.objects.all()


class PostDetailAPIView(ListAPIView):
    serializer_class = PostsSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'


class PostUpdateAPIView(UpdateAPIView):
    serializer_class = PostsSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
    # permission_classes = (permissions.IsAuthenticated, IsOwner,)


class PostDestroyAPIView(DestroyAPIView):
    serializer_class = PostsSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
    # permission_classes = (permissions.IsAuthenticated, IsOwner,)
