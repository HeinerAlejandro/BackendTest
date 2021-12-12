from django.db import models

# Create your models here.


class Poll(models.Model):
    class AgeTypes(models.Choices):
        FROM_18_25 = '18-25'
        FROM_26_33 = '26-33'
        FROM_34_40 = '34-40'
        MORE_40 = '40+'

    class SocialNetworkTypes(models.Choices):
        FACEBOOK = 'facebook'
        WHATSAPP = 'whatsapp'
        TWITTER = 'twitter'
        INSTAGRAM = 'instagram'
        TIKTOK = 'tiktok'

    class GenderTypes(models.Choices):
        MALE = "male"
        FEMALE = "female"

    email = models.EmailField('email', unique=True)
    age = models.CharField('age', max_length=5, choices=AgeTypes.choices)
    gender = models.CharField('gender', max_length=9, choices=GenderTypes.choices)
    favorite_social_network = models.CharField(max_length=9, choices=SocialNetworkTypes.choices)

    time_facebook_avg = models.DecimalField('time facebook avg', max_digits=4, decimal_places=2)
    time_whatsapp_avg = models.DecimalField('time whatsapp avg', max_digits=4, decimal_places=2)
    time_twitter_avg = models.DecimalField('time twitter avg', max_digits=4, decimal_places=2)
    time_instagram_avg = models.DecimalField('time instagram avg', max_digits=4, decimal_places=2)
    time_tiktok_avg = models.DecimalField('time tiktok avg', max_digits=4, decimal_places=2)