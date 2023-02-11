from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Profile, Bill, Budget
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

        def __init__(self, *args, **kwargs):
            super(RegisterForm, self).__init__(*args, **kwargs)
            self.fields['email'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['class'] = 'form-control'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

        widgets = {
            "mobile_no" : forms.TextInput(attrs={"class" : "form-control", "placeholder": "Enter your number"}),
            "profile_pic" : forms.FileInput(attrs={"class" : "form-control", "type":"file", "placeholder": "Choose your profile picture"}),
            "creditcard_no" : forms.TextInput(attrs={"class" : "form-control", "placeholder": "Enter a valid credit card"}),
            "income_amount" : forms.TextInput(attrs={"class" : "form-control", "placeholder": "Kindly indicate your monthly income"}),
            "income_date" : forms.DateInput(attrs={"class" : "form-control", "type": "date", "placeholder": "Kindly indicate your income date"}) 
        }

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        exclude = ['user']

        widgets = {
            "name" : forms.Select(attrs={"class" : "form-select"}),
            "amount" : forms.TextInput(attrs={"class" : "form-control",}),
            "date" : forms.DateInput(attrs={"class" : "form-control", "type": "date"})  
        }

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        exclude = ['user']

        widgets = {
            "budget" : forms.Select(attrs={"class" : "form-select"}),
            "payment_method" : forms.Select(attrs={"class" : "form-select",}),
            "payment_details" : forms.TextInput(attrs={"class" : "form-control"})  
        }

