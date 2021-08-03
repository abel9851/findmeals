from django.db import models


class Food(models.Model):
    """Food Model Definition"""

    name = models.CharField(max_length=50)
