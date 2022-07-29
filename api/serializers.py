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
    class Meta:
        model = Profile
        fields = ['id', 'patronymic', 'user','code','position','subdivision','user','avatar','salary']


    def create(self, validated_data):
        user_data = validated_data.pop('user')
        positions = validated_data.pop('position')
        user = User.objects.create(**user_data)
        profile = Profile.objects.create(user=user, **validated_data)
        for position in positions:
            profile.position.add(position)
        return profile






class PositionSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True, read_only=True)
    class Meta:
        model = Position
        fields = ['id', 'name', 'parent','children']

class SubdivisionSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True, read_only=True)
    class Meta:
        model = Subdivision
        fields = ['id', 'name', 'parent','children']

