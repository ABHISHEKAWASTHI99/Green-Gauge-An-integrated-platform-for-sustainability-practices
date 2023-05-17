from django import forms
from .models import Contact, feedback

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


class feedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['feedback_type', 'feedback']

        