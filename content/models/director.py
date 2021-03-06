from django.db import models

class Director(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    
    class Meta:
        app_label = 'content'

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'