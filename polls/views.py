from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.viewsets import mixins

from .serializers import PollSerializer

# Create your views here.


class PollAPIView(mixins.CreateModelMixin,
                  viewsets.GenericViewSet):

    serializer_class = PollSerializer

