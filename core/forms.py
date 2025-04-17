from django import forms
from .models import Ingredient, Menu

class IngredientForm(forms.ModelForm):
    menu = forms.ModelChoiceField(queryset=Menu.objects.all(), required=True)

    class Meta:
        model = Ingredient
        fields = ['ingredientName', 'menu']
