from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)', views.TutorRequestRetrieveDestroyAPIView.as_view(), name='detail'),
    url(r'^list-create', views.TutorRequestListCreateAPIView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)', views.TutorRequestUpdate.as_view(), name='update')
]
