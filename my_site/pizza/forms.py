from django import forms
from .models import Pizza


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['company', 'pizza_type', 'dough', 'image', 'description']


class PizzaSearchForm(forms.Form):
    name = forms.CharField(required=False)
    description = forms.CharField(required=False)
    price = forms.DecimalField(required=False)
    dough_type = forms.CharField(required=False)
    company = forms.CharField(required=False)

