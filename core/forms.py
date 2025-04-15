from django import forms

class MenuForm(forms.Form):
    foodName = forms.CharField(max_length=250)

class IngredientForm(forms.Form):
    ingredientName = forms.CharField(max_length=250)
