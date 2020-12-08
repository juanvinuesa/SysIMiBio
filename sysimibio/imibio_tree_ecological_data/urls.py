from django.urls import path

from sysimibio.imibio_tree_ecological_data.views import new

app_name = 'imibio_tree_ecological_data'

urlpatterns = [
    path('', new, name='new'),
]
