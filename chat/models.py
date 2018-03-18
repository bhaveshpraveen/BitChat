from django.conf import settings
from django.db import models
from django.urls import reverse


class Room(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.slug.title())

    def get_absolute_url(self):
        return reverse('room', kwargs={'room_name': self.slug})


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='messages', on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text