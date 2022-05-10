from django.shortcuts import render
from rest_framework import generics
# generic

from .models import Post
from .serializers import PostSerializer

# CBV

#ListCreateAPIView
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#RetrieveUpdateDestroyAPIView
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

