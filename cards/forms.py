from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class AddCardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")

        super(AddCardForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Список не выбран"
        self.fields['category'].queryset = Category.objects.filter(user=self.request.user)

    class Meta:
        model = Card
        fields = ['category', 'title_native_language', 'translate_studied_language',
                  'usage_example', 'photo']
        widgets = {
            'usage_example': forms.Textarea(attrs={'cools': 60, 'rows': 10}),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')