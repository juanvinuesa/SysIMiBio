from django import forms
from django.core.exceptions import ValidationError
from datetime import date


def validate_fecha(value):
    if value > date.today():
        raise ValidationError('Fecha debe estar en el formato AAAA-MM-DD y debe ser menor o igual a la fecha de hoy',
                              'fecha')


def validate_temp(temp):
    if temp < -5 or temp > 45:
        raise ValidationError('Temperatura debe estar en un rango desde -5 hasta 45° Celsius',
                              'temperatura')


def validate_humedad(humedad):
    if humedad < 0 or humedad > 100:
        raise ValidationError('Humedad debe estar en un rango desde 0 hasta 100%',
                              'humedad')


def validate_lat(lat):
    if lat < -28.17 or lat > -25.48:
        raise ValidationError('Latitud no corresponde a Misiones',
                              'latitud')


def validate_lon(lon):
    if lon < -56.06 or lon > -53.62:
        raise ValidationError('Longitud no corresponde a Misiones',
                              'longitud')


class TreeEcologicalForm(forms.Form):
    fecha = forms.DateField(help_text='ej.: AAAA-MM-DD', validators=[validate_fecha])
    hora_inicio = forms.TimeField(help_text='ej.: 12:30')
    hora_final = forms.TimeField(help_text='ej.: 13:00')
    temperatura = forms.FloatField(help_text='°C', validators=[validate_temp])
    humedad = forms.FloatField(help_text='%', validators=[validate_humedad])
    responsable = forms.CharField()
    acompanantes = forms.CharField(label='Acompañantes')
    id_parcela = forms.IntegerField()
    id_arbol = forms.IntegerField()
    especie = forms.CharField()
    dap = forms.FloatField(help_text='cm')  # todo a partir de que DAP se va a medir?
    dab = forms.FloatField(help_text='cm')  # todo a partir de que DAB se va a medir?
    altura = forms.FloatField(help_text='m')  # todo a partir de que altura se va a medir?
    latitud = forms.FloatField(validators=[validate_lat])
    longitud = forms.FloatField(validators=[validate_lon])
    fotografia = forms.URLField(help_text='ej.: http://www.drive.google.com/fotos_parcelaX', required=False)
    obs = forms.CharField()
    estado_arbol = forms.CharField()
    forma_vida = forms.CharField()
    clasificacion_sociologica = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        start_time = self.cleaned_data.get('hora_inicio')
        end_time = self.cleaned_data.get('hora_final')
        if start_time is not None and end_time is not None and start_time > end_time:
            raise ValidationError("Hora de inicio debe ser menor que hora final")
        return cleaned_data
