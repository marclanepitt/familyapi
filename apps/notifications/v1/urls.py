from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^list/(?P<user>\d)', views.NotificationListView.as_view(), name='user_notification_list'),
    url(r'^create',views.NotificationCreateView.as_view(),name='notification_create'),
    url(r'^update/(?P<pk>\d)', views.NotificationUpdateView.as_view(),name='update_notification'),
    url(r'^read/(?P<pk>\d)/(?P<user>\d)',views.NotificationReadView.as_view(),name="set_read_notification"),
    url(r'^posts/list/(?P<family>\d)',views.PostListView.as_view(),name="post_list"),
    url(r'^posts/create',views.PostCreateView.as_view(),name="post_create"),
    url(r'^posts/like/(?P<pk>\d)',views.PostLikeView.as_view(),name="post_like"),
    url(r'^posts/unlike/(?P<pk>\d)',views.PostUnlikeView.as_view(),name="post_unlike"),
]
