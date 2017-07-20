from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^institutions', views.InstitutionListView.as_view(), name='institutions-list'),
    url(r'^majors', views.MajorListView.as_view(), name='institutions-list'),
]
