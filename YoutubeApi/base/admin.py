from django.contrib import admin
from . import models
# Register your models here.
class VideoList(admin.ModelAdmin):
    list_display = ("Title",)
admin.site.register(models.ListOfVideos, VideoList)
