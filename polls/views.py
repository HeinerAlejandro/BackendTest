from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.viewsets import mixins

from .models import Poll
from .serializers import PollSerializer

# Create your views here.


class PollAPIView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):

    queryset = Poll.objects.all()
    serializer_class = PollSerializer


