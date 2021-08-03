from django.contrib import admin
from . import models


@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):

    """Food Admin Definition"""

    pass
