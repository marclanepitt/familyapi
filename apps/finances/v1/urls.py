from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^charges/(?P<family>\d)', views.ChargeListView.as_view(), name='charge-list'),
    url(r'^charges/create', views.ChargeCreateView.as_view(), name ='charge-create'),
]
