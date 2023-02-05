from django.db import models

class ListOfVideos(models.Model):
    Title = models.CharField(
        null=True,
        blank=True,
        max_length=500
    )

    Description = models.TextField(
        null=True,
        blank=True,
    )

    VideoId = models.CharField(
        null=False,
        blank=False,
        max_length=150,
    )
        
    ChannelId = models.CharField(
        null=False,
        blank=False,
        max_length=150
    )

    ChannelName = models.CharField(
        null=False,
        blank=False,
        max_length=100
    )

    Duration = models.FloatField()

    UploadDateTime = models.DateTimeField()

    ThumbnailUrl = models.URLField()

    VideoUrl = models.URLField()

    def __str__(self):
        return self.Title




