from django.contrib import admin
from django.core.exceptions import ValidationError
from sysimibio.imibio_tree_ecological_data.forms import FieldForm, PicturesForm, TreeForm
from sysimibio.imibio_tree_ecological_data.models import TreeEcologicalData, Tree, Pictures


class PicsInline(admin.TabularInline):
    form = PicturesForm
    model = Pictures


class TreeInline(admin.StackedInline):
    form = TreeForm
    model = Tree
    extra = 1
    inlines = [PicsInline]
    exclude = ('geom',)


class TreeEcologicalDataModelAdmin(admin.ModelAdmin):
    form = FieldForm
    inlines = [TreeInline]
    list_display = ('date', 'coordinator', 'start_time', 'end_time', 'parcel_id', 'created_at', 'last_modification_at')
    date_hierarchy = 'date'
    search_fields = ('date', 'coordinator', 'parcel_id')
    list_filter = ('date', 'coordinator', 'parcel_id')


admin.site.register(TreeEcologicalData, TreeEcologicalDataModelAdmin)
admin.site.register(Pictures)
