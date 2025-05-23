from django import forms
from .models import Ingredient, Food, Reservation, Order


class IngredientForm(forms.ModelForm):
    food = forms.ModelChoiceField(queryset=Food.objects.all(), required=True)

    class Meta:
        model = Ingredient
        fields = ["ingredientName", "food"]


class ReservationForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}))

    class Meta:
        model = Reservation
        fields = ["hostName", "name", "phone", "partySize", "date", "time", "allergy"]

    def clean_partySize(self):
        party_size = self.cleaned_data["partySize"]
        if party_size < 1:
            raise forms.ValidationError("Party size must be at least 1")
        return party_size

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields["hostName"].initial = self.user.get_full_name()
            self.fields["hostName"].widget = forms.HiddenInput()


class OrderForm(forms.Form):
    name = forms.CharField(label="Name for your order", max_length=32)
    time = forms.DateTimeField()
    food_list = forms.MultipleChoiceField(
        choices=[], required=True
    )  # Empty initial choices
    notes = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Preserving your exact loop logic
        foods = []
        id = 0
        for i in Food.objects.all():
            id += 1
            foods.append((id, i.foodName))
        self.fields["food_list"].choices = foods
