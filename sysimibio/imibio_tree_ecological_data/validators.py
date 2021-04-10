from django.core.exceptions import ValidationError
from datetime import date


def validate_date(value):
    if value > date.today():
        raise ValidationError('Fecha debe estar en el formato AAAA-MM-DD y debe ser menor o igual a la fecha de hoy',
                              'date')


def validate_temperature(temp):
    if temp < -5 or temp > 45:
        raise ValidationError('Temperatura debe estar en un rango desde -5 hasta 45° Celsius',
                              'temperature')


def validate_humidity(humedad):
    if humedad < 0 or humedad > 100:
        raise ValidationError('Humedad debe estar en un rango desde 0 hasta 100%',
                              'humidity')


def validate_lat(lat):
    if lat < -28.17 or lat > -25.48:
        raise ValidationError('Latitud no corresponde a Misiones',
                              'latitude')


def validate_lon(lon):
    if lon < -56.06 or lon > -53.62:
        raise ValidationError('Longitud no corresponde a Misiones',
                              'longitude')
