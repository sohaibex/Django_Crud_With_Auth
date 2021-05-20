from django import forms
from .models import Cdr

class CdrForms(forms.ModelForm):
    class Meta:
        model = Cdr
        fields = "__all__"