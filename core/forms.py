from django import forms
from .models import Ingredient, Menu, Reservation
# -----------------------------------------------
# Form for ingredients (existing)
# -----------------------------------------------

class IngredientForm(forms.ModelForm):
    menu = forms.ModelChoiceField(queryset=Menu.objects.all(), required=True)

    class Meta:
        model = Ingredient
        fields = ['ingredientName', 'menu']

    # ---------------------------------------
    # Forms for Reservation (Gabriel Task)
    # ---------------------------------------

    class ReservationForm(forms.ModelForm):
        class Meta:
            model = Reservation
            fields = ['partySize', 'date', 'time']
            widgets = {
                'date': forms.DateInput(attrs={'type': 'date'}),
                'time': forms.TimeInput(attrs={'type': 'time'}),
            }

