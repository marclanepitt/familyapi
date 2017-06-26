from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+|me)', views.UserDetailView.as_view(), name='detail')
]
