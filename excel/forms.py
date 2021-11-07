from django import forms
from .models import Xlsx, XlsxData

class XlsxModelForm(forms.ModelForm):
    class Meta:
        model = Xlsx
        fields = ('file_name',)



class EditForm(forms.ModelForm):
    class Meta:
        model = XlsxData
        fields = '__all__'
