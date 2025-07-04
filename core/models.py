from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser


class Reservation(models.Model):
    hostName = models.CharField(max_length=32, default="none")
    name = models.CharField(max_length=32, default="none")
    phone = models.CharField(max_length=20, blank=True)
    partySize = models.PositiveSmallIntegerField(default=1)
    date = models.DateField(default=timezone.now)
    time = models.TimeField("Time", default=timezone.now)
    allergy = models.CharField(max_length=500, default="none")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1
    )

    def save(self, *args, **kwargs):
        if not self.hostName:  # Set default hostName to owner's name
            self.hostName = self.owner.get_full_name()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.hostName}'s party"


class Ingredient(models.Model):
    ingredientName = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.ingredientName}"


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Food(models.Model):
    foodName = models.CharField(max_length=250)
    ingredients = models.ManyToManyField("Ingredient", blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f'{self.foodName} (contains: {", ".join([i.ingredientName for i in self.ingredients.all()])}) -- ${self.price}'


class Order(models.Model):
    hostName = models.CharField(max_length=32, default=" ")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1
    )
    time = models.DateTimeField(default=timezone.now)
    notes = models.CharField(max_length=256, default="")

    def __str__(self):
        return f"{self.hostName}s Order"


class ItemsOrder(models.Model):
    foodName = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=3)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.quantity} orders of {self.foodName}"


class Event(models.Model):
    eventName = models.CharField(max_length=255)
    day = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    location = models.CharField(max_length=255)
    eventDescription = models.TextField()
    image = models.ImageField(upload_to="event_images/", blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="events_created",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.eventName} ({self.day.strftime('%B %d, %Y')})"


class News(models.Model):
    title = models.CharField(max_length=100)
    news = models.TextField()

    def __str__(self):
        return f"{self.title}"
