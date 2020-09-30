from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CompressedGasCylinder


class DraftForm(UserCreationForm):
    inspection_id = forms.IntegerField()
    cylinder_id = forms.CharField(max_length=50)
    date = forms.CharField(max_length=50)


    class Meta:
        model = CompressedGasCylinder
        fields = ('inspection_id', 'cylinder_id', 'date')