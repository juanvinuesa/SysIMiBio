from django import forms


class TreeEcologicalForm(forms.Form):
    fecha = forms.DateField()
    hora_inicio = forms.TimeField()
    hora_final = forms.TimeField()
    temperatura= forms.FloatField()
    humedad = forms.FloatField()
    responsable = forms.CharField()
    acompanantes = forms.CharField()
    id_parcela = forms.CharField()
    id_arbol = forms.IntegerField()
    especie = forms.CharField()
    dap = forms.FloatField()
    dab = forms.FloatField()
    altura = forms.FloatField()
    latitud = forms.FloatField()
    longitud = forms.FloatField()
    fotografia = forms.BooleanField()
    obs = forms.CharField()
    estado_arbol = forms.CharField()
    forma_vida = forms.CharField()
    clasificacion_sociologica = forms.CharField()
