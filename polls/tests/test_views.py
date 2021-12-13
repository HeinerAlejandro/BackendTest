from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.response import Response


class TestPollViewSet(APITestCase):
    def setUp(self) -> None:
        self.__polls = [
            {
                'email': 'heiner.enis@gmail.com',
                'gender': 'male',
                'age': '18-25',
                'favorite_social_network': 'facebook',
                'time_facebook_avg': 2.5,
                'time_whatsapp_avg': 1.3,
                'time_twitter_avg': 0.8,
                'time_instagram_avg': 1,
                'time_tiktok_avg': 0.4
            },
            {
                'email': 'heiner.enis@gmail.com',
                'gender': 'male',
                'age': '20',
                'favorite_social_network': 'Bumble',
                'time_facebook_avg': 2.5,
                'time_whatsapp_avg': 1.3,
                'time_twitter_avg': 0.8,
                'time_instagram_avg': 1,
                'time_tiktok_avg': 0.4
            },
            {
                'email': 'other.person@gmail.com',
                'gender': 'male',
                'age': '40+',
                'favorite_social_network': 'whatsapp',
                'time_facebook_avg': 5.5,
                'time_whatsapp_avg': 8.3,
                'time_twitter_avg': 9.8,
                'time_instagram_avg': 1,
                'time_tiktok_avg': 0.8
            }
        ]

    def __consume_api_create(self, url_name, index_poll) -> Response:

        url = reverse(url_name)

        poll = self.__polls[index_poll]

        response = self.client.post(
            url,
            poll,
            format='json'
        )

        return response

    def test_create_poll_success(self):

        response = self.__consume_api_create('polls-list', 0)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_create_poll_error(self):

        self.__consume_api_create('polls-list', 0)
        response = self.__consume_api_create('polls-list', 1)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

        keys_response = response.data.keys()

        self.assertIn('email', keys_response)
        self.assertIn('age', keys_response)
        self.assertIn('favorite_social_network', keys_response)

    def test_get_polls_success(self):
        url = reverse('polls-list')

        self.__consume_api_create('polls-list', 0)
        self.__consume_api_create('polls-list', 2)

        response = self.client.get(url)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(len(response.data), 2)

    def test_most_used_sn_per_age_success(self):

        url = reverse('polls-most-used-sn-per-age')

        self.__consume_api_create('polls-list', 0)
        self.__consume_api_create('polls-list', 2)

        response = self.client.get(url)

        self.assertEquals(response.status_code, status.HTTP_200_OK)