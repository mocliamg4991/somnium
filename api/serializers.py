from turtle import position
from profiles.models import Profile
from organization.models import Position, Subdivision
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name','username']

class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    position = serializers.StringRelatedField(many=True)
    

    class Meta:
        model = Profile
        fields = ['id', 'patronymic', 'user','code','position','user','avatar','salary']


class PositionSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)
    parent = serializers.StringRelatedField()
    class Meta:
        model = Position
        fields = ['id', 'name', 'parent','children']

class SubdivisionSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)
    parent = serializers.StringRelatedField()
    class Meta:
        model = Subdivision
        fields = ['id', 'name', 'parent','children']

