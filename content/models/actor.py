from django.db import models

class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    bod = models.DateField(null=True, blank=True)

    class Meta:
        app_label = 'content'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'