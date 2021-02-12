from django.contrib import admin
from sysimibio.imibio_tree_ecological_data.models import TreeEcologicalData

class TreeEcologicalDataModelAdmin(admin.ModelAdmin):
    list_display = ('date', 'coordinator', 'start_time', 'end_time', 'parcel_id')

admin.site.register(TreeEcologicalData, TreeEcologicalDataModelAdmin)
