from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^chores/(?P<family>\d)', views.ChoreListView.as_view(), name='chore'),
    url(r'^chores/available/(?P<family>\d)', views.ChoreAvailableListView.as_view(), name='chore_available'),
    url(r'^chores/user/(?P<user_profile>\d)', views.ChoreListUserView.as_view(), name='chore_user'),
    url(r'^chores/update/(?P<pk>\d)/', views.ChoreUpdateView.as_view(), name='chore_update'),
    #url(r'^chores/create/(?P<family>\d)', views.ChoreCreateView.as_view(), name='chore-create'),
]
