from django.contrib import admin
from . import models


@admin.register(models.list)
class ListAdmin(admin.ModelAdmin):

    """List Admin Definition"""

    pass
