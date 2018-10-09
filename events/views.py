# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets,permissions
from .models import events
from .serializers import eventsSerializer
# Create your views here.

class eventsView(viewsets.ModelViewSet):
	queryset = events.objects.all()
	serializer_class = eventsSerializer