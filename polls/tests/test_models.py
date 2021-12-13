from django.test import TestCase

from polls.models import Poll
from polls.choices import AgeTypes


class TestPollModels(TestCase):
    def setUp(self) -> None:
        self.__polls = [
            {
                'email': 'heiner.enis@gmail.com',
                'gender': 'male',
                'age': '18-25',
                'favorite_social_network': 'facebook',
                'time_facebook_avg': 10.5,
                'time_whatsapp_avg': 1.3,
                'time_twitter_avg': 0.8,
                'time_instagram_avg': 1,
                'time_tiktok_avg': 0.4
            },
            {
                'email': 'other1.enis@gmail.com',
                'gender': 'male',
                'age': '26-33',
                'favorite_social_network': 'twitter',
                'time_facebook_avg': 2.5,
                'time_whatsapp_avg': 12.3,
                'time_twitter_avg': 0.8,
                'time_instagram_avg': 1,
                'time_tiktok_avg': 0.4
            },
            {
                'email': 'other2.person@gmail.com',
                'gender': 'male',
                'age': '40+',
                'favorite_social_network': 'whatsapp',
                'time_facebook_avg': 5.5,
                'time_whatsapp_avg': 8.3,
                'time_twitter_avg': 9.8,
                'time_instagram_avg': 1,
                'time_tiktok_avg': 22.3
            }
        ]

    def test_get_age_range_success(self):

        for poll in self.__polls:
            Poll.objects.create(**poll)

        age_range = Poll.objects.age_most_uses_sn(Poll.SocialNetworkTypes.FACEBOOK)

        self.assertEquals(age_range, AgeTypes.FROM_18_25.value)

        age_range = Poll.objects.age_most_uses_sn(Poll.SocialNetworkTypes.WHATSAPP)

        self.assertEquals(age_range, AgeTypes.FROM_26_33.value)

        age_range = Poll.objects.age_most_uses_sn(Poll.SocialNetworkTypes.TIKTOK)

        self.assertEquals(age_range, AgeTypes.MORE_40.value)

    def test_get_age_range_none(self):

        age_range = Poll.objects.age_most_uses_sn(Poll.SocialNetworkTypes.FACEBOOK)

        self.assertEquals(age_range, AgeTypes.FROM_18_25.value)

        age_range = Poll.objects.age_most_uses_sn(Poll.SocialNetworkTypes.WHATSAPP)

        self.assertEquals(age_range, AgeTypes.FROM_18_25.value)

        age_range = Poll.objects.age_most_uses_sn(Poll.SocialNetworkTypes.TIKTOK)

        self.assertEquals(age_range, AgeTypes.FROM_18_25.value)