from django.db import models


class AgeTypes(models.Choices):
    FROM_18_25 = '18-25'
    FROM_26_33 = '26-33'
    FROM_34_40 = '34-40'
    MORE_40 = '40+'
