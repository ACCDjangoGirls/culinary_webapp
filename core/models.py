from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class Reservation(models.Model):
    partySize = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(20)]
    )
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)

    #-------------------------------------------------
    # Guest contact info and allergy tracking
    # ----------------------------------------------
    guest_name = models.CharField(max_length=100, default="Guest", blank=True)
    guest_email = models.EmailField(default="guest@email.com", blank=True)
    guest_phone = models.CharField(max_length=15, default="000000000000000", blank=True)
    special_request = models.TextField(blank=True, default="")
    allergies = models.ManyToManyField('Allergy', blank=True)

    def __str__(self):
        return f'{self.guest_name} - Party of {self.partySize} - on {self.date.strftime("%B %d, %y")} at {self.time.strftime("%I:%M %p")}'

    class Meta:
        ordering = ['date', 'time']
    # Relationship to Allergies(If needed later)
class Allergy(models.Model):
    SEVERITY_CHOICES = [
        ('mild', 'Mild'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe')
    ]
    name = models.CharField(max_length=100)
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES)

    def __str__(self):
        return f'{self.name} ({self.severity})'
    #+host name????
    #allergy foreign key has been deleted. haven't made the Allergy model yet
    #for date/time formatting:
    #https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior:~:text=strptime(date_string%2C%20format)-,strftime()%20and%20strptime()%20Format%20Codes,-%C2%B6
    
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
        return self.ingredientName
        
class Food(models.Model):
    foodName = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    ingredients = models.ManyToManyField('Ingredient', blank=True)

    available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.foodName}'
    
class Order(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    ORDER_TYPES = [
        ('takeout','Takeout'),
        ('dine-in','Dine_In'),
    ]
    order_type = models.CharField(max_length=10, choices=ORDER_TYPES, default='dine-in')
    created_at = models.DateTimeField(default=timezone.now)

    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f'{self.foodName} (contains: {", ".join([i.ingredientName for i in self.ingredients.all()])}) -- ${self.price}'
    
class Order(models.Model):
    hostName = models.CharField(max_length=32, default=' ')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    time = models.TimeField(default=timezone.now)

    
    def __str__(self):

        return f'order #{self.id} for {self.reservation.guest_name}'
    
class ItemsOrder(models.Model):
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)

        return f'{self.name} at {self.time.strftime("%b %d, %I:%M %p")}'
    
class ItemsOrder(models.Model):
    foodName = models.ForeignKey(Food, on_delete=models.CASCADE)

    quantity = models.CharField(max_length=3)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', null=True)
    special_instructions = models.TextField(blank=True, default="")

    def __str__(self):

        return f'{self.quantity} orders of {self.menu_item} (order #{self.order.id})'

        return f"{self.quantity} orders of {self.foodName}"


class Event(models.Model):
    eventName = models.CharField(max_length=200)
    day = models.DateField(default=timezone.now)
    startTime = models.TimeField()
    endTime = models.TimeField()
    location = models.CharField(max_length=100)
    eventDescription = models.TextField()
    max_attendees = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):

        return f'{self.eventName} ({self.day.strftime("%B %d, %Y")})'
      
        return f"{self.eventName} ({self.day.strftime("%B %d, %Y")})"

class News(models.Model):
    title = models.CharField(max_length=100)
    news = models.TextField()

    def __str__(self):
        return f'{self.title}'

