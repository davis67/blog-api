from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import PostsSerializer, CommentSerializer

from .permissions import IsOwner
from .models import Post


class ImageUploadParser(FileUploadParser):
    media_type = 'image/*'


class PostCreateAPIView(CreateAPIView):

    serializer_class = PostsSerializer

    parser_class = (ImageUploadParser,)

    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        author = self.request.user
        return serializer.save(author=author)


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer


class PostDetailAPIView(RetrieveAPIView):

    serializer_class = PostsSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'


class PostUpdateAPIView(UpdateAPIView):
    serializer_class = PostsSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
    permission_classes = (permissions.IsAuthenticated, IsOwner,)



class PostDestroyAPIView(DestroyAPIView):
    serializer_class = PostsSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
    permission_classes = (permissions.IsAuthenticated, IsOwner,)


class CommentCreateAPIView(CreateAPIView):

    serializer_class = CommentSerializer

    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        author = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        print(post)
        return serializer.save(author=author, post=post)

