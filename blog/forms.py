from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['person', 'number', 'email', 'event', 'file']
        
    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file and file.size > 10 * 1024 * 1024:  # 10 MB
            raise forms.ValidationError("File size must not exceed 10 MB.")
        return file

import pandas as pd

def handle_excel_upload(file):
    df = pd.read_excel(file)
    return df