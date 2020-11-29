from django import forms


class TreeEcologicalForm(forms.Form):
    fecha = forms.CharField()
    hora_inicio = forms.CharField()
    hora_final = forms.CharField()
    temperatura= forms.CharField()
    humedad = forms.CharField()
    responsable = forms.CharField()
    acompanante = forms.CharField()
    id_arbol = forms.CharField()
    especie = forms.CharField()
    dap = forms.CharField()
    dab = forms.CharField()
    altura = forms.CharField()
    latitud = forms.CharField()
    longitud = forms.CharField()
    fotografia = forms.CharField()
    obs = forms.CharField()
    estado_arbol = forms.CharField()
    forma_vida = forms.CharField()
    clasificacion_sociologica = forms.CharField()
