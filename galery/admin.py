from django.contrib import admin
from galery.models import Picture

class picture_list_view(admin.ModelAdmin):
    list_display = ("id", "name", "credits", "published")
    list_display_links =("id", "name")
    list_editable = ("published",)
    search_fields = ("name",)
    list_filter = ("category","published")
    list_per_page = 10

admin.site.register(Picture, picture_list_view)
