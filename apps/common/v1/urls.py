from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^pets/create/(?P<family>\d)', views.PetCreateView.as_view(), name='pet-create'),
    url(r'^pets/list/(?P<family>\d)', views.PetListView.as_view(), name='pet-list'),
    url(r'^family/(?P<family>\d)', views.FamilyListView.as_view(), name='family'),
]
