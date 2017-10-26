from rest_framework import generics,mixins
from .serializers import NotificationSerializer,NotificationCountSerializer,PostSerializer
from django.shortcuts import get_object_or_404
from ..models import Notification,Post
from users.models import UserProfile

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationCountSerializer

    def get_queryset(self):
        return Notification.objects.filter(notify__in=self.kwargs['user'])

    def get_serializer_context(self):
        return {'user': self.kwargs['user']}

class NotificationCreateView(generics.CreateAPIView):
	serializer_class = NotificationSerializer

class NotificationUpdateView(generics.GenericAPIView, mixins.UpdateModelMixin):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class NotificationReadView(generics.ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        notification = Notification.objects.get(pk=self.kwargs['pk'])
        notification.read_by.add(get_object_or_404(UserProfile,pk=self.kwargs['user']))
        notification.save()
        return Notification.objects.filter(notify__in = self.kwargs['user'])

class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(family=self.kwargs['family'])

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer

class PostLikeView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        post = Post.objects.get(pk = self.kwargs['pk'])
        post.likes = post.likes + 1
        post.save()
        return post

class PostUnlikeView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        post = Post.objects.get(pk = self.kwargs['pk'])
        post.likes = post.likes - 1
        post.save()
        return post