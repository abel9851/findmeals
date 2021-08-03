from django.db import models
from core import models as core_models


class Food(core_models.TimeStampedModel):
    """Food Model Definition"""

    name = models.CharField(max_length=50)
