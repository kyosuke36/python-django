from django.db import models


class Event(models.Model):
    event_text = models.CharField(max_length=200)

    def __str__(self):
        return self.event_text


class Choice(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
