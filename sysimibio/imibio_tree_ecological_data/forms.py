from django import forms
from django.core.exceptions import ValidationError
from django.contrib import admin
from sysimibio.imibio_tree_ecological_data.models import Tree, TreeEcologicalData, Pictures


class TreeForm(forms.ModelForm):
    class Meta:
        model = Tree
        fields = '__all__'
        exclude = ['geom']


class FieldForm(forms.ModelForm):
    class Meta:
        model = TreeEcologicalData
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        if start_time > end_time:
            raise ValidationError("Hora de inicio debe ser menor que hora final")
        return cleaned_data


class PicturesForm(forms.ModelForm):
    class Meta:
        model = Pictures
        fields = '__all__'
