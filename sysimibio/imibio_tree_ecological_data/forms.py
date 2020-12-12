from django import forms
from django.core.exceptions import ValidationError

from sysimibio.imibio_tree_ecological_data.models import TreeEcologicalData


class TreeEcologicalForm(forms.Form):
    fecha = forms.DateField(help_text='ej.: AAAA-MM-DD')
    hora_inicio = forms.TimeField(help_text='ej.: 12:30')
    hora_final = forms.TimeField(help_text='ej.: 13:00')
    temperatura= forms.FloatField(help_text='°C')
    humedad = forms.FloatField(help_text='%')
    responsable = forms.CharField()
    acompanantes = forms.CharField(label='Acompañantes')
    id_parcela = forms.CharField()
    id_arbol = forms.IntegerField()
    especie = forms.CharField()
    dap = forms.FloatField(help_text='cm')
    dab = forms.FloatField(help_text='cm')
    altura = forms.FloatField(help_text='m')
    latitud = forms.FloatField()
    longitud = forms.FloatField()
    fotografia = forms.BooleanField(required=False)
    obs = forms.CharField()
    estado_arbol = forms.CharField()
    forma_vida = forms.CharField()
    clasificacion_sociologica = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('hora_inicio')
        end_time = cleaned_data.get('hora_final')
        if start_time > end_time:
            raise forms.ValidationError("Hora inicial debe ser menor que hora final")
        return cleaned_data
