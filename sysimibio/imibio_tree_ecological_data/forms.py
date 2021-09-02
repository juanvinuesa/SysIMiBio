from django import forms
from django.core.exceptions import ValidationError
from django.forms import HiddenInput
from geojson import Point
from leaflet.forms.widgets import LeafletWidget

from sysimibio.imibio_tree_ecological_data.models import Tree, FieldWork, Pictures, PermanentParcel, TreeMeasurement


class TreeForm(forms.ModelForm):
    class Meta:
        model = Tree
        fields = '__all__'
        widgets = {
            'geom': HiddenInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        lon = cleaned_data.get('longitude')
        lat = cleaned_data.get('latitude')
        cleaned_data["geom"] = Point((lon, lat))
        if not cleaned_data["geom"].is_valid:
            raise ValidationError("Geometria inválida")
        return cleaned_data


class FieldForm(forms.ModelForm):
    class Meta:
        model = FieldWork
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        if (start_time and end_time) and start_time > end_time:
            raise ValidationError("Hora de inicio debe ser menor que hora final")
        return cleaned_data


class PicturesForm(forms.ModelForm):
    class Meta:
        model = Pictures
        fields = '__all__'


class PermanentParcelForm(forms.ModelForm):
    class Meta:
        model = PermanentParcel
        exclude = ('created_at',)
        widgets = {
            'geom': LeafletWidget(),
        }


class TreeMeasurementForm(forms.ModelForm):
    class Meta:
        model = TreeMeasurement
        fields = '__all__'
