import operator

from django.db.models import Avg, Count

from rest_framework import viewsets
from rest_framework.viewsets import mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Poll
from .serializers import PollSerializer, MostUsedPerAgeSerializer

# Create your views here.


class PollAPIView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):

    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    @action(detail=False, methods=['get',], url_path='most-used-per-age', serializer_class=MostUsedPerAgeSerializer)
    def most_used_sn_per_age(self, request):
        """Return Most Used Social Networks per Age Range"""

        serializer_class = self.get_serializer_class()

        serializer = serializer_class({
            'facebook': Poll.objects.age_most_uses_sn(Poll.SocialNetworkTypes.FACEBOOK),
            'whatsapp': Poll.objects.age_most_uses_sn(Poll.SocialNetworkTypes.WHATSAPP),
            'twitter': Poll.objects.age_most_uses_sn(Poll.SocialNetworkTypes.TWITTER),
            'instagram': Poll.objects.age_most_uses_sn(Poll.SocialNetworkTypes.INSTAGRAM),
            'tiktok': Poll.objects.age_most_uses_sn(Poll.SocialNetworkTypes.TIKTOK)
        })

        return Response(serializer.data)


