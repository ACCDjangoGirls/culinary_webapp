from django import forms
from .models import Ingredient, Foods

class IngredientForm(forms.ModelForm):
    menu = forms.ModelChoiceField(queryset=Foods.objects.all(), required=True)

    class Meta:
        model = Ingredient
        fields = ['ingredientName', 'menu']
