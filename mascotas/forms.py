from django import forms
from .models import Reptil, Ave, Anfibio

class ReptilForm(forms.ModelForm):
    class Meta:
        model = Reptil
        fields = '__all__'

class AveForm(forms.ModelForm):
    class Meta:
        model = Ave
        fields = '__all__'

class AnfibioForm(forms.ModelForm):
    class Meta:
        model = Anfibio
        fields = '__all__'

class BuscarMascotaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    especie = forms.ChoiceField(choices=[('Reptil', 'Reptil'), ('Ave', 'Ave'), ('Anfibio', 'Anfibio')])
