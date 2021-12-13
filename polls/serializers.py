from rest_framework import serializers

from .models import Poll


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class MostUsedPerAgeSerializer(serializers.Serializer):
    facebook = serializers.CharField()
    whatsapp = serializers.CharField()
    instagram = serializers.CharField()
    twitter = serializers.CharField()
    tiktok = serializers.CharField()