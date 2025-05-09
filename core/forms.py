from django import forms
from .models import Ingredient, Food

class IngredientForm(forms.ModelForm):
    food = forms.ModelChoiceField(queryset=Food.objects.all(), required=True)

    class Meta:
        model = Ingredient
        fields = ['ingredientName', 'food']

class OrderForm(forms.Form):
    name = forms.CharField(label="Name for your order", max_length=32)
    time = forms.DateTimeField()

    foods = []
    id = 0
    emptyList = []
    for i in Food.objects.all():
        id += 1
        foods.append((id,i.foodName)) 

    food_list = forms.MultipleChoiceField(choices=foods, required=True)

    notes = forms.CharField(widget=forms.Textarea)
