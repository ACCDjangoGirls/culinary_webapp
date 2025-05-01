from django import forms
from .models import Ingredient, Food

class IngredientForm(forms.ModelForm):
    menu = forms.ModelChoiceField(queryset=Food.objects.all(), required=True)

    class Meta:
        model = Ingredient
        fields = ['ingredientName', 'menu']
