from django.db import models
from django.utils import timezone

class Reservation(models.Model):
    partySize = models.PositiveSmallIntegerField()
    date = models.DateField(default=timezone.now)
    time = models.TimeField("P", default=timezone.now)
    
    #+host name????
    #allergy foreign key has been deleted. haven't made the Allergy model yet
    #for date/time formatting:
    #https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior:~:text=strptime(date_string%2C%20format)-,strftime()%20and%20strptime()%20Format%20Codes,-%C2%B6
    def __str__(self):
        return f'Party of {self.partySize} on {self.date.strftime('%B %d, %Y')} at {self.time.strftime('%I:%M%p')}'
       
class Ingredient(models.Model):
    ingredientName = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.ingredientName}'
        
class Menu(models.Model):
    foodName = models.CharField(max_length=250)
    ingredients = models.ManyToManyField('Ingredient')

    def __str__(self):
        return f'{self.foodName} (contains: {", ".join([i.ingredientName for i in self.ingredients.all()])})'
    
class Order(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    ORDER_TYPES = [
        ('takeout','Takeout'),
        ('dine-in','Dine_In'),
    ]
    takeout = models.CharField(max_length=10, choices=ORDER_TYPES, default='dine-in')

    def __str__(self):
        return f'{self.reservation}'
    
class ItemsOrder(models.Model):
    foodName = models.ForeignKey(Menu, on_delete=models.CASCADE)
    order = models.ManyToManyField('Order')
    quantity = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.quantity} orders of {self.foodName}'

class Event(models.Model):
    eventName = models.CharField(max_length=200)
    day = models.DateField(default=timezone.now)
    startTime = models.TimeField()
    endTime = models.TimeField()
    location = models.CharField(max_length = 100)
    eventDescription = models.TextField()

    def __str__(self):
        return f'{self.eventName} ({self.day.strftime('%B %d, %Y')})'

class News(models.Model):
    title = models.CharField(max_length=100)
    news = models.TextField()

    def __str__(self):
        return f'{self.title}'
