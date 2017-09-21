from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^pets/create', views.PetCreateView.as_view(), name='pet-create'),
    url(r'^family/(?P<family>\d)', views.FamilyListView.as_view(), name='family')
]
