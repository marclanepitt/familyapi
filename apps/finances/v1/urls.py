from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^charges/(?P<family>\d)', views.ChargeListView.as_view(), name='charge'),
    url(r'^charges/create/(?P<family>\d)', views.ChargeCreateView.as_view(), name='charge-create'),
]
