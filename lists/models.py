from django.db import models
from core import models as core_models


class list(core_models.TimeStampedModel):

    """List Model Definition"""

    name = models.CharField(max_length=50)
    user = models.ForeignKey(
        "users.User", related_name="lists", on_delete=models.CASCADE
    )
    foods = models.ManyToManyField("foods.Food", related_name="lists", blank=True)

    def __str_(self):
        return self.name
