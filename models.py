from django.db import models

class Reservation(models.Model):
    partySize = models.PositiveSmallIntegerField()
    dateTime = models.DateTimeField()
    
    #allergy foreign key has been deleted. haven't made the Allergy model yet
    def __str__(self):
        return (self.partySize, self.dateTime)
       
class Menu(models.Model):
    foodName = models.CharField(max_length=250)
    ingredients = models.ManyToManyField(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return (self.foodName, self.ingredients)
    
class Ingredient(models.Model):
    ingredientName = models.CharField(max_length=250)

    def __str__(self):
        return (self.ingredientName)
    
class Order(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    ORDER_TYPES = [
        ('takeout','Takeout'),
        ('dine-in','Dine_In'),
        ('catering','Catering'),
    ]
    takeout = models.CharField(max_length=10, choices=ORDER_TYPES, default='dine-in')

    def __str__(self):
        return (self.reservation)
    
class ItemsOrder(models.Model):
    foodName = models.ForeignKey(Menu, on_delete=models.CASCADE)
    order = models.ManyToManyField(Order, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=3)

    def __str__(self):
        return (self.foodName)

class Takeout(models.Model):
    
    def __str__(self):
        return (self) #ummmmmm help what goes in here/in this model??

class Event(models.Model):
    eventName = models.CharField(max_length=200)
    startTime = models.TimeField()
    endTime = models.TimeField()
    location = models.CharField(max_length = 100)
    eventDescription = models.TextField()

    def __str__(self):
        return (self.eventName)
