from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Ingredient, Menu, Reservation, Allergy, Food, Order


class IngredientForm(forms.ModelForm):
    food = forms.ModelChoiceField(queryset=Food.objects.all(), required=True)
    class Meta:
        model = Ingredient
        fields = ['ingredientName','food']
        widgets = {
            'ingredientName': forms.TextInput(attrs={
                'Placeholder': 'Enter Ingredient name',
                'class': 'form-control'
            })
        }
        
class ReservationForm(forms.ModelForm):
    allergies = forms.ModelMultipleChoiceField(
        queryset=Allergy.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Any allergies we should know about?'
    )
    class Meta:
        model = Reservation
        fields = [
            'name', 'guest_email', 'phone',
            'partySize', 'date', 'time', 'special_request', 'allergies'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'guest_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'partySize': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 20}),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'min': timezone.now().date(),
                'class': 'form-control'
            }),
            'time':forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control'
            }),
            'special_request': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Allergies, high chair, etc.',
                'class': 'form-control'
            })
        }
    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date and date < timezone.now().date():
            raise ValidationError("Reservation cannot be made for past date.")
        return date
    
    def clean_partySize(self):
        partySize = self.cleaned_data.get('partySize')
        if partySize is not None:
            if partySize < 1:
                raise ValidationError("Party size must be at least one.")
            if partySize > 20:
                raise ValidationError("Party sizes more than twenty(20), please call us directly.")
        return partySize
    
    def clean_time(self):
        time = self.cleaned_data.get('time')
        if time and (time.hour < 11 or time.hour > 23):
            raise ValidationError("We only accept reservations between 11 AM and 11 PM.")
        return time
    

class MenuForm(forms.ModelForm):
    Ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta:
        model = Menu
        fields = ['foodName', 'description', 'price', 'available', 'ingredients']
        widgets = {
            'foodName': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows':3, 'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'step':'0.01', 'class': 'form-control'}),
            'available': forms.CheckboxInput(),
        }

class OrderForm(forms.ModelForm):
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Order
        fields = ['hostName', 'owner', 'time']

def __init__(self, *args, **kwargs):
    self.user = kwargs.pop('user', None)
    super().__init__(*args, **kwargs)
    if self.user:
        self.fields['hostName'].initial = self.user.get_full_name()
        self.fields['hostName'].widget = forms.HiddenInput()
