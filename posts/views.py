from django.shortcuts import render
from rest_framework import generics
# generic

from .models import Post
from .serializers import PostSerializer

from django.shortcuts import render
import json
import os
from django.http import HttpResponse
from os import path

# CBV

#ListCreateAPIView
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#RetrieveUpdateDestroyAPIView
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


file1 = "testingData/"


def jsonview(request):
    file_path = os.getcwd() + "/" + path.relpath(file1)
    # print("path :", os.getcwd())
    # print("json ", file_path)
    data = dict()

    with open(file_path + '/BookData.json', 'r') as file_handler:
        data = json.load(file_handler)

    return HttpResponse(json.dumps(data), content_type='application/json')

import feedparser
# Python에서 feed를 파싱할 수 있는 feedparser 라이브러리
# 뉴스를 제공하고 있는 곳에서 제공되는 RSS주소를 통해 들어가면, 기사의 타이틀과 링크들을 가져올수 있음

def viewfeed(request):
    feeds = feedparser.parse('http://johnsmallman.wordpress.com/author/johnsmallman/feed/')
    #feeds = feedparser.parse('http://www.espn.com/espn/rss/news')
    return render(request, "viewFeed.html", {'feeds' : feeds})

def viewjson(request):
    return render(request, 'viewJSON.html')

def viewrest(request):
    return render(request, 'viewREST.html')

