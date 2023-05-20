from django import forms
from .models import post


class postForm(forms.modelForm):
    class Meta:
        model = post
        fields = '__all__'