from django import forms
from accounts.models import Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Complaint'})
        }