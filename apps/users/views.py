from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from apps.users.models import MainUser, Role
from apps.users.serializers import MainUserSerializer, RoleSerializer


class UserCreateApiView(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = MainUser.objects.all()
    serializer_class = MainUserSerializer


class RolesListView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
