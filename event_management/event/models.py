from django.db import models
from django.shortcuts import reverse
from django.conf import settings

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=100)
    slug = models.SlugField()
    description_short = models.CharField(max_length=50)
    description_long = models.TextField()
    image = models.ImageField()
    max_available_seats = models.PositiveIntegerField(default=0)
    no_of_ticket_sold = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("event:event_detail", kwargs={
            'slug': self.slug
        })



class Slide(models.Model):
    caption1 = models.CharField(max_length=100)
    caption2 = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    image = models.ImageField(help_text="Size: 1920x570")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{} - {}".format(self.caption1, self.caption2)


class Booked_Event(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    booked_date = models.DateTimeField(auto_now_add=True)
    event =  models.ForeignKey(Event,on_delete=models.CASCADE)
    no_of_tickets = models.PositiveIntegerField(default=0)
    total_price = models.FloatField(default=0)
