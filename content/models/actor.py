from django.db import models

class Actor(models.Model):
    actor_id = models.CharField(primary_key=True, max_length= 10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    bod = models.DateField(null=True, blank=True)

    class Meta:
        app_label = 'content'

    def __str__(self):
        return f'{self.actor_id}, {self.first_name}, {self.last_name}, {self.bio}'