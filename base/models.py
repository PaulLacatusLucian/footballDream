from django.db import models


class Room(models.Model):
    # host =
    # topic
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_created=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    nr_of_participants = models.IntegerField(default=0)
    current_participants = models.IntegerField(default=0)
    time_of_game = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.name