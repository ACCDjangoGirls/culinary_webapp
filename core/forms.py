from django import forms
from .models import Ingredient, Food, Reservation, Order

class IngredientForm(forms.ModelForm):
    food = forms.ModelChoiceField(queryset=Food.objects.all(), required=True)

    class Meta:
        model = Ingredient
        fields = ['ingredientName', 'food']

class ReservationForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Reservation
        fields = ['hostName', 'partySize', 'date', 'time', 'allergy']

class OrderForm(forms.ModelForm):
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Order
        fields = ['hostName', 'owner', 'time']