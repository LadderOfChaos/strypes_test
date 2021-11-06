from django import forms
from .models import Xlsx

class CsvModelForm(forms.ModelForm):
    class Meta:
        model = Xlsx
        fields = ('file_name',)
