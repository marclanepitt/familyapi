from rest_framework import serializers
from ..models import Notification, Post
from users.models import UserProfile
import datetime
import math

class NotificationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Notification
		fields=("id","notify","message","link","app","read_by","time",)

class NotificationCountSerializer(serializers.ModelSerializer):
	time_ago = serializers.SerializerMethodField()
	unread_count = serializers.SerializerMethodField()
	is_read = serializers.SerializerMethodField()

	class Meta:
		model = Notification
		fields=("id","notify","message","link","app","read_by","unread_count","is_read","time","time_ago")

	def get_unread_count(self,obj):
		unreadCount = 0
		for n in Notification.objects.filter(notify__in=self.context['user']):
			is_read = False
			for u in n.read_by.all():
				if u.id == int(self.context['user']):
					is_read = True
			if not is_read:
				unreadCount += 1
		return unreadCount

	def get_is_read(self,obj):
		is_read = False
		for u in obj.read_by.all():
			if u.id == int(self.context['user']):
				is_read = True
				break
		return is_read

	def get_time_ago(self,obj):
		result = datetime.datetime.now()-obj.time.replace(tzinfo=None)
		if 'day' in str(result):
			if(result.days > 365):
				if(result.days < 365*2):
					return "1 year"
				else:
					return str(math.floor(result.days / 365)) + " years"
			elif 'days' in str(result):
				return str(result).split(" ")[0] + " days"
			else:
				return str(result).split(" ")[0] + " day"				
		else:
			a = str(result).split(":")
			if a[0] is not '0':
				if a[0] is '1':
					return a[0]+ " hour"
				else:
					return a[0] + " hours"
			elif a[1] is not '0':
				if a[1] is '1':
					return a[1] + "minute"
				else:
					return a[1] + " minutes"
			else:
				return a[2] + " seconds"

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ("family","message","date_created","posted_by")