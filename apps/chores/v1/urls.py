from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^chores/(?P<family>\d)', views.ChoreListView.as_view(), name='chore'),
    url(r'^chores/(?P<family>\d)/(?P<user_profile>\d)', views.ChoreListUserView.as_view(), name='chore_user'),
    #url(r'^chores/create/(?P<family>\d)', views.ChoreCreateView.as_view(), name='chore-create'),
]
