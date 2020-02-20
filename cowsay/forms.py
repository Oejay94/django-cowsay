from django import forms
from cowsay.models import Cowsay

class TextInput(forms.ModelForm):
    class Meta:
        model = Cowsay
        fields = '__all__'
    