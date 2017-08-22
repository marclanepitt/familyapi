from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^charges/(?P<family>\d)', views.ChargeListCreateView.as_view(), name='charge'),
]
