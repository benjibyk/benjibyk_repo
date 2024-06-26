from django.db import models

class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=8)

    def __str__(self):
        return self.short_url