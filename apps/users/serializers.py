from rest_framework import serializers

from apps.users.models import MainUser


class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ['iin', 'phone', 'email', 'password', 'first_name', 'last_name', 'middle_name']
