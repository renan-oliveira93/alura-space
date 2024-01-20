from django.contrib import admin
from galery.models import Picture

class picture_list(admin.ModelAdmin):
    list_display = ("id", "name", "credits")
    list_display_links =("id", "name")
    search_fields = ("name",)

admin.site.register(Picture, picture_list)
