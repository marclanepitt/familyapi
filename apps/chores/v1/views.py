from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from knox.auth import TokenAuthentication
from rest_framework import generics,mixins
from rest_framework.response import Response
from users.models import UserProfile
from django.db.models.aggregates import Sum
import datetime

from .utils import LeaderboardPagination
from .serializers import ChoreListSerializer,ChoreUpdateSerializer,ChoreLeaderBoardSerializer,ChoreRewardSerializer,ChoreRewardRedeemSerializer,ChoreCompleteSerializer
from ..models import Chore,ChoreReward

class ChoreListView(generics.ListAPIView):
    serializer_class = ChoreListSerializer
    def get_queryset(self):
        family = self.kwargs['family']
        return Chore.objects.filter(family=family)
class ChoreListUserView(generics.ListAPIView):
    serializer_class = ChoreListSerializer
    def get_queryset(self):
        user_profile = self.kwargs['user_profile']
        family = UserProfile.objects.get(pk= user_profile).family.id
        return Chore.objects.filter(family=family,participants__in=user_profile)

class ChoreAvailableListView(generics.ListAPIView):
    serializer_class = ChoreListSerializer
    def get_queryset(self):
        family = self.kwargs['family']
        return Chore.objects.filter(family=family, participants=None)

class ChoreUpdateView(generics.GenericAPIView, mixins.UpdateModelMixin):
    queryset = Chore.objects.all()
    serializer_class = ChoreUpdateSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class ChoreCompleteView(generics.ListAPIView):
    serializer_class = ChoreCompleteSerializer

    def get_queryset(self):
        chore = Chore.objects.get(pk=self.kwargs['pk'])
        chore.is_completed = True
        chore.completed_date = datetime.datetime.now()
        chore.save()
        for user in chore.participants.all():
            user.chore_points = user.chore_points + chore.num_points
            user.save()
        return UserProfile.objects.filter(pk = self.kwargs['user'])

class ChoreLeaderBoardView(generics.ListAPIView):
    serializer_class = ChoreLeaderBoardSerializer
    pagination_class = LeaderboardPagination
    def get_queryset(self):
        leaderboard = []
        family = self.kwargs['family']
        for user in UserProfile.objects.filter(family = family):
            numPoints = Chore.objects.filter(participants=user.id, is_completed=True).aggregate(Sum('num_points'))
            if numPoints['num_points__sum'] is None:
                numPoints['num_points__sum'] = 0
            leaderboard.append({"user":user,"num_points":numPoints['num_points__sum']})
        max_points = 0    
        for d in leaderboard:
            if d.get('num_points') > max_points:
                max_points = d.get('num_points')
        for d in leaderboard:
            d['max_points'] = max_points        
        return leaderboard

class ChoreRewardListView(generics.ListAPIView):
    serializer_class = ChoreRewardSerializer
    def get_queryset(self):
        user_profile = self.kwargs['user_profile']
        return ChoreReward.objects.filter(rewarded_to = user_profile)

class ChoreRewardUpdateView(generics.GenericAPIView, mixins.UpdateModelMixin):
    queryset = ChoreReward.objects.all()
    serializer_class = ChoreRewardSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class ChoreRewardRedeemView(generics.GenericAPIView, mixins.UpdateModelMixin):
    queryset = ChoreReward.objects.all()
    serializer_class = ChoreRewardRedeemSerializer

    def put(self, request, *args, **kwargs):
        chore_reward = ChoreReward.objects.get(pk = request.data['id'])
        profile = UserProfile.objects.get(pk = chore_reward.rewarded_to.id)
        if profile.chore_points >= chore_reward.num_points and not chore_reward.is_redeemed:
            profile.chore_points = profile.chore_points - chore_reward.num_points
            profile.save()
            return self.partial_update(request, *args, **kwargs)
        else:
            return Response({"response":"This is already redeemed"})