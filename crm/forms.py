from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'fecha_in': forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_sal': forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
