from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from apps.users.models import MainUser
from apps.users.serializers import MainUserSerializer


class UserCreateApiView(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = MainUser.objects.all()
    serializer_class = MainUserSerializer
