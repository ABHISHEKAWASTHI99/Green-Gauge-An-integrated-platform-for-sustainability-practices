from django import forms
from .models import Merchandise

class MerchandiseForm(forms.ModelForm):
    class Meta:
        model = Merchandise
        fields = ('name', 'description', 'price', 'image',)
        