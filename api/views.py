from profiles.models import Profile
from organization.models import Subdivision, Position
from api.serializers import ProfileSerializer, PositionSerializer, SubdivisionSerializer
from rest_framework import generics


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer



class PositionList(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer



class SubdivisionList(generics.ListCreateAPIView):
    queryset = Subdivision.objects.all()
    serializer_class = SubdivisionSerializer

