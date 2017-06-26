from django.conf.urls import include, url

urlpatterns = [
    url(r'^users/', include('users.v1.urls', namespace='users')),
]
