from rest_framework import generics,permissions
from rest_framework import viewsets
from . import serializers
from django.contrib.auth.models import User
from .models import Like, Post
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status

from django.http import JsonResponse, HttpResponse



import json
from .permissions import IsOwnerOrReadOnly
from .mixins import LikedMixin

class RegisterApi(generics.GenericAPIView):
    serializer_class = serializers.RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": serializers.UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class ActivityUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserActivitySerializer



class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class PostList(LikedMixin,viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

class PostAnaliticsLikesView(generics.ListAPIView):
    serializer_class = serializers.LikeSerializer

    def get(self, request, *args, **kwargs):
        likes_analitic = Like.objects.filter(like_published__range=[kwargs['date_from'], kwargs['date_to']])
        if len(likes_analitic) > 0:
            mimetype = 'application/json'
            return HttpResponse(json.dumps({'likes by period': len(likes_analitic)}), mimetype)
        else:
            return self.list(request, *args, [{}])