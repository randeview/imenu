from rest_framework import serializers

from apps.restaurant.models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['name', 'address', 'description']

    def create(self, validated_data):
        owner = self.context['owner']
        organization = Organization(owner=owner, **validated_data)
        organization.save()
        validated_data['owner'] = owner.email
        return validated_data
