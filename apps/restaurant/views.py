from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import OrganizationSerializer
from rest_framework import mixins, viewsets, status
from .models import Organization


class CreateOrganizationView(GenericAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def get_serializer_context(self):
        context = super(CreateOrganizationView, self).get_serializer_context()
        context.update({'owner': self.request.user})
        return context

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data=data, status=status.HTTP_201_CREATED)
