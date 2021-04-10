from django import forms
from django.core.exceptions import ValidationError
from sysimibio.imibio_tree_ecological_data.validators import validate_date, validate_temperature, validate_humidity, validate_lat, validate_lon
# from datetime import date
#
#
# def validate_date(value):
#     if value > date.today():
#         raise ValidationError('Fecha debe estar en el formato AAAA-MM-DD y debe ser menor o igual a la fecha de hoy',
#                               'fecha')
#
#
# def validate_temperature(temp):
#     if temp < -5 or temp > 45:
#         raise ValidationError('Temperatura debe estar en un rango desde -5 hasta 45° Celsius',
#                               'temperatura')
#
#
# def validate_humidity(humedad):
#     if humedad < 0 or humedad > 100:
#         raise ValidationError('Humedad debe estar en un rango desde 0 hasta 100%',
#                               'humedad')
#
#
# def validate_lat(lat):
#     if lat < -28.17 or lat > -25.48:
#         raise ValidationError('Latitud no corresponde a Misiones',
#                               'latitud')
#
#
# def validate_lon(lon):
#     if lon < -56.06 or lon > -53.62:
#         raise ValidationError('Longitud no corresponde a Misiones',
#                               'longitud')


class TreeEcologicalForm(forms.Form):
    date = forms.DateField(help_text='ej.: AAAA-MM-DD', validators=[validate_date])
    start_time = forms.TimeField(help_text='ej.: 12:30')
    end_time = forms.TimeField(help_text='ej.: 13:00')
    temperature = forms.FloatField(help_text='°C', validators=[validate_temperature])
    humidity = forms.FloatField(help_text='%', validators=[validate_humidity])
    coordinator = forms.CharField()
    staff = forms.CharField(label='Acompañantes')
    parcel_id = forms.IntegerField()
    tree_id = forms.IntegerField() # to be create as "ParcelaXArbolY"
    specie = forms.CharField()
    dap = forms.FloatField(help_text='cm')  # todo a partir de que DAP se va a medir?
    dab = forms.FloatField(help_text='cm')  # todo a partir de que DAB se va a medir?
    tree_height = forms.FloatField(help_text='m')  # todo a partir de que altura se va a medir?
    latitude = forms.FloatField(validators=[validate_lat]) # todo add aclaración de que se esta usando WSG84
    longitude = forms.FloatField(validators=[validate_lon])
    picture = forms.FileField(help_text='Choose foto', required=False) # todo add file. a tree can have more than one pictures. 1:n
    obs = forms.CharField()
    phytosanitary_status = forms.CharField()
    sociological_classification = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')
        if start_time is not None and end_time is not None and start_time > end_time:
            raise ValidationError("Hora de inicio debe ser menor que hora final")
        return cleaned_data
