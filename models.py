from django.db import models

class Reservation(models.Model):
    partySize = models.CharField(max_length=3)
    time = models.CharField(max_length=5)
    
    allergy = models.ForeignKey(Account, on_delete=models.CASCADE)
    username = models.ForeignKey(Account, on_delete=models.CASCADE)
    def __str__(self):
        return self.partySize, self.allergy, self.time, self.username
    

class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    allergy = models.CharField(max_length=250)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)

    def __str__(self):
        return self.username, self.password, self.email, self.allergy, self.firstName, self.lastName
    
class Menu(models.Model):
    foodName = models.CharField(max_length=250)
    ingredients = models.ManyToManyField(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return self.foodName, self.ingredients
    
class Ingredient(models.Model):
    ingredientName = models.CharField(max_length=250)

    def __str__(self):
        return self.ingredientName
    
class Order(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)

    def __str__(self):
        return self.reservation
    
class ItemsOrder(models.Model):
    foodName = models.ForeignKey(Menu, on_delete=models.CASCADE)
    order = models.ManyToManyField(Order, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=3)

    def __str__(self):
        return self.foodName

