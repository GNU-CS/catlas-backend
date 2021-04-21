from datetime import datetime, timezone

from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from api import serializers
from api.models import Post
from api.permissions import IsOwner

class ListAPI(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.ListPostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class GetAPI(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class CreateAPI(generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            post_data = {
                'title': request.data['title'],
                'date_created': datetime.now(timezone.utc),
                'views': 0,
                'content': request.data['content'],
                'user': request.data['user']
            }

            serializer = self.get_serializer(data=post_data)
            serializer.is_valid(raise_exception=True)

            serializer.save()
            
            return Response({'success': 'Post successfully created.'}, status=status.HTTP_201_CREATED)

        except KeyError:
            return Response({'error': 'Invalid request body.'}, status=status.HTTP_400_BAD_REQUEST)

class UpdateAPI(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticated & IsOwner]

    def patch(self, request, *args, **kwargs):
        try:
            post = self.get_object()
            post.content = request.data['content']
            post.save()
            
            return Response(status=status.HTTP_204_NO_CONTENT)

        except KeyError as e:
            return Response({'error': 'Invalid request body.'}, status=status.HTTP_400_BAD_REQUEST)

class DeleteAPI(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticated & IsOwner]

    def delete(self, request, *args, **kwargs):
        try:
            return self.destroy(request, *args, **kwargs)

        except KeyError as e:
            return Response({'error': 'Invalid request body.'}, status=status.HTTP_400_BAD_REQUEST)