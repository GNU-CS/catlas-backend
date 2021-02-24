from datetime import datetime, timezone
from hashlib import sha256
from secrets import token_hex

from django.contrib.auth.models import User
from django.http.response import Http404

from rest_framework import generics, mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from knox.auth import AuthToken, TokenAuthentication

from api import serializers
from api.models import Board, Post

# Create your views here.

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

class PostViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    @action(methods=['POST'], detail=False, authentication_classes=(TokenAuthentication,), permission_classes=(IsAuthenticated,))
    def write(self, request):
        try:
            post_data = {
                'post_type': int(Board.TALKS),
                'title': request.data['title'],
                'date_created': datetime.now(timezone.utc),
                'views': 0,
                'content': request.data['content'],
                'user': request.data['user']
            }

            serializer = self.get_serializer(data=post_data)

            serializer.is_valid(raise_exception=True)

            serializer.save()

            return Response({
                'success': 'Post successfully created!'
            }, status=status.HTTP_201_CREATED)

        except KeyError:
            return Response({
                'error': 'Invalid value!'
            }, status=status.HTTP_400_BAD_REQUEST)

    # Add IsOwner permission
    @action(methods=['PATCH'], detail=True, authentication_classes=(TokenAuthentication,), permission_classes=[IsAuthenticated])
    def modify(self, request, pk=None):
        try:
            post = self.get_object()

            post.content = request.data['content']

            post.save()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except AssertionError as e:
            return Response({
                'error': 'Invalid value!'
        }, status=status.HTTP_400_BAD_REQUEST)
        
    # Add IsOwner permission
    @action(methods=['DELETE'], detail=True, authentication_classes=(TokenAuthentication,), permission_classes=[IsAuthenticated])
    def delete(self, request, pk=None):
        try:
            post = self.get_object()

            post.delete()

            return Response({
                'success': 'Post successfully deleted!'
            }, status=status.HTTP_204_NO_CONTENT)

        except AssertionError:
            return Response({
                'error': 'Cannot delete all post at once!'
            }, status=status.HTTP_400_BAD_REQUEST)