from rest_framework import serializers

from apps.users.models import MainUser, Role


class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ['iin', 'phone', 'email', 'password', 'first_name', 'last_name', 'middle_name', 'role']

    def create(self, validated_data):
        user = MainUser(**validated_data)
        user.save()
        return validated_data


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
