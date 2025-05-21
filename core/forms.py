from django import forms
from .models import Ingredient, Food

class IngredientForm(forms.ModelForm):
    food = forms.ModelChoiceField(queryset=Food.objects.all(), required=True)

    class Meta:
        model = Ingredient
        add-ownership-and-images-to-events
        fields = ['ingredientName', 'food']


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
