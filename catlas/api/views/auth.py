from rest_framework import generics

from knox.auth import AuthToken

from api import serializers

class LoginAPI(generics.GenericAPIView):
    serializer_class = serializers.LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data

        return Response({
            'user': serializers.UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1], # AuthToken.objects.create(user) returns tuple (instance, token)
        }, status=status.HTTP_200_OK)

class RegistrationAPI(generics.GenericAPIView):
    serializer_class = serializers.CreateUserSerializer

    def post(self, request, *args, **kwargs):
        try:
            request.data['email'] += '@gnu.ac.kr'

            serializer = self.get_serializer(data=request.data)
            
            serializer.is_valid(raise_exception=True)

            # Implement E-mail authentication

            user = serializer.save()

            return Response({}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ResetAPI(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        email = request.data['email'] + '@gnu.ac.kr'
        
        # Implement E-mail authentication

        return Response({}, status=status.HTTP_200_OK)

class CheckAPI(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        return Response({
            'detail': 'Valid token.'
        }, status=status.HTTP_200_OK)