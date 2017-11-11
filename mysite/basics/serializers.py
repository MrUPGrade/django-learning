from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Contact, Tag





class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name')


class ContactSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'email', 'tags', 'phone', 'user')
        depth = 0
