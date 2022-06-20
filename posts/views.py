from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics,permissions

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerilizer
    permission_classes = (permissions.IsAdminUser)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated)  
    queryset = Post.objects.all()
    serializer_class = PostSerilizer
