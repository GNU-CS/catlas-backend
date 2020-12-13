from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.serializers import CreateMemberSerializer

# Create your views here.

class RegistrationAPI(GenericAPIView):
    serializer_class = CreateMemberSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)

        return Response(
            {
                "response": 'pong'
            }
        )

        