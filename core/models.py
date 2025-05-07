from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.conf import settings

class Reservation(models.Model):
    hostName = models.CharField(max_length=32, default="none")
    partySize = models.PositiveSmallIntegerField(default=1)
    date = models.DateField(default=timezone.now)
    time = models.TimeField("P", default=timezone.now)
    allergy = models.CharField(max_length=500, default="none")
    
    def __str__(self):
        return f"{self.hostName}'s party"
       
class Ingredient(models.Model):
    ingredientName = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.ingredientName}'
        
class Food(models.Model):
    foodName = models.CharField(max_length=250)
    ingredients = models.ManyToManyField('Ingredient', blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f'{self.foodName} (contains: {", ".join([i.ingredientName for i in self.ingredients.all()])}) -- ${self.price}'
    
class Order(models.Model):
    hostName = models.CharField(max_length=32, default=' ')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    time = models.TimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.name} at {self.time.strftime("%b %d, %I:%M %p")}'
    
class ItemsOrder(models.Model):
    foodName = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=3)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.quantity} orders of {self.foodName}"

class Event(models.Model):
    eventName = models.CharField(max_length=200)
    day = models.DateField(default=timezone.now)
    startTime = models.TimeField()
    endTime = models.TimeField()
    location = models.CharField(max_length = 100)
    eventDescription = models.TextField()

    def __str__(self):
        return f"{self.eventName} ({self.day.strftime('%B %d, %Y')})"

class News(models.Model):
    title = models.CharField(max_length=100)
    news = models.TextField()

    def __str__(self):
        return f'{self.title}'
