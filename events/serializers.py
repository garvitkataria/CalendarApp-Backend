from rest_framework import serializers
from .models import events

class eventsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = events
		fields = ('id','description','completed','startTime', 'endTime', 'allDay', 'title')