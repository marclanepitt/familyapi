from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+|me)', views.UserDetailView.as_view(), name='detail'),
    url(r'^profile', views.UserProfileCreateView.as_view(), name='profile-create'),
    url(r'^list/(?P<id>\d)', views.UserProfileListView.as_view(), name='profile-detail'),
    url(r'^update/(?P<pk>\d)', views.UserProfileUpdateView.as_view(), name='profile-update'),
    url(r'^login/(?P<id>\d)', views.UserProfileLoginView.as_view(), name='profile-login')
]
