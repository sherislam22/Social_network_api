from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import  Post,Like



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'last_name')
        extra_kwargs = {
            'password':{'write_only': True},
            }

    def create(self, validated_data):
        user = User.objects.create_user(
        validated_data['username'],
        password = validated_data['password'],
        first_name=validated_data['first_name'], 
        last_name=validated_data['last_name']
        )

        return user


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username']

class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'last_login',
        )



class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Post
        fields = ['id', 'created','title','body','owner', 'total_likes']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
             'like_published',
             'user'
        )

