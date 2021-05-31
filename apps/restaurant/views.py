from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class CreateOrganizationView(GenericAPIView):
    # permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        print(request.user)
        return Response('ok')
