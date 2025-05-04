from django import forms
from .models import Ingredient, Menu

class IngredientForm(forms.ModelForm):
    menu = forms.ModelChoiceField(queryset=Menu.objects.all(), required=True)

    class Meta:
        model = Ingredient
        fields = ['ingredientName', 'menu']


from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['eventName', 'day', 'startTime', 'endTime', 'location', 'eventDescription', 'image']
        widgets = {
            'startTime': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'endTime': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'day': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
