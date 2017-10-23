from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<family>\d)', views.ChoreListView.as_view(), name='chore'),
    url(r'^available/(?P<family>\d)', views.ChoreAvailableListView.as_view(), name='chore_available'),
    url(r'^user/(?P<user_profile>\d)', views.ChoreListUserView.as_view(), name='chore_user'),
    url(r'^update/(?P<pk>\d)/', views.ChoreUpdateView.as_view(), name='chore_update'),
    url(r'^complete/(?P<pk>\d)/(?P<user>\d)/', views.ChoreCompleteView.as_view(), name='chore_update'),
    url(r'^leaderboard/(?P<family>\d)/', views.ChoreLeaderBoardView.as_view(),name='chore_leaderboard'),
    url(r'^rewards/(?P<user_profile>\d)/',views.ChoreRewardListView.as_view(), name='chore_rewards'),
    url(r'^rewards/update/(?P<pk>\d)/', views.ChoreRewardUpdateView.as_view(), name='chore_rewards_update'),
    url(r'^rewards/redeem/(?P<pk>\d)/', views.ChoreRewardRedeemView.as_view(), name='chore_rewards_redeem'),    
    #url(r'^chores/create/(?P<family>\d)', views.ChoreCreateView.as_view(), name='chore-create'),
]
