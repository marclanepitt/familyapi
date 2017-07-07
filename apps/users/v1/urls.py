from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+|me)', views.UserDetailView.as_view(), name='detail'),
    url(r'^profile', views.UserProfileCreateView.as_view(), name='profile-create'),
]
