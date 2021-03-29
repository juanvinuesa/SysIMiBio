from django.contrib import admin
from sysimibio.imibio_tree_ecological_data.models import TreeEcologicalData, Tree, Pictures


class PicsInline(admin.TabularInline):
    model = Pictures


class TreeInline(admin.TabularInline):
    model = Tree
    inlines = [PicsInline]
    exclude = ('geom',)


class TreeEcologicalDataModelAdmin(admin.ModelAdmin):
    inlines = [TreeInline]
    list_display = ('date', 'coordinator', 'start_time', 'end_time', 'parcel_id', 'created_at', 'last_modification_at')
    date_hierarchy = 'date'
    search_fields = ('date', 'coordinator', 'parcel_id')
    list_filter = ('date', 'coordinator', 'parcel_id')


admin.site.register(TreeEcologicalData, TreeEcologicalDataModelAdmin)
admin.site.register(Pictures)