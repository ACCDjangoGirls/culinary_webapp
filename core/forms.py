from django import forms
from .models import Ingredient, Menu

class IngredientForm(forms.ModelForm):
    menu = forms.ModelChoiceField(queryset=Menu.objects.all(), required=True)

    class Meta:
        model = Ingredient
        fields = ['ingredientName', 'menu']


from .models import Event

class EventForm(forms.ModelForm):
    start_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}))
    end_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}))

    class Meta:
        model = Event
        fields = '__all__'
