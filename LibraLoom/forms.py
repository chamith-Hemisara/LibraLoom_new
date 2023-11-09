# library_app/forms.py
from django import forms
from .models import Book, Category

class AdvancedSearchForm(forms.Form):
    title = forms.CharField(required=False)
    author = forms.CharField(required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)


from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(widget=forms.Textarea, label='Your Message')
