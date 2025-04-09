from django.db import models

# Create your models here.

class Ingredient(models.Model):
    ingredientName = models.CharField(max_length=250)

    def __str__(self):
        return (self.ingredientName)
