from django import forms
from .models import *


class AddCardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        print(self.request)
        super(AddCardForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Список не выбран"
        self.fields['category'].queryset = Category.objects.filter(user=self.request.user)
        # self.fields['user'] = Card.objects.filter(user=self.request.user)
    class Meta:
        model = Card
        fields = ['category', 'title_native_language', 'translate_studied_language',
                  'usage_example', 'photo']
        widgets = {
            'usage_example': forms.Textarea(attrs={'cools': 60, 'rows': 10}),
        }
