from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=200, blank=True)

    class Meta:
        app_label = 'content'
        
    def __str__(self):
        return self.name