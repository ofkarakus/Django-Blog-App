from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# !!! UserCreationForm(forms.ModelForm) !!!
class RegistrationForm(UserCreationForm):
    
    email = forms.EmailField()  # = forms.EmailField(required=True) => default

    class Meta:
        model = User
        fields = ('username', 'email')

    # If you want to add custom validation for any field, 
    # you need to use "clean_" keyword in the name of method as a prefix.
    def clean_email(self):  
        email = self.cleaned_data['email']  # = email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another email. That one is already token.')
        return email
