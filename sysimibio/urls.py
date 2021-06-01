"""sysimibio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView

import sysimibio.core.views
from sysimibio.imibio_tree_ecological_data import views as v


urlpatterns = [
    path('', sysimibio.core.views.home, name='home'), # todo melhorar esse import
    path('admin/', admin.site.urls),
    path('registro_ocurrencias/', include('sysimibio.imibio_occurrences.urls')), # todo cambiar a ingles
    path('registro_ecologico_arboreas/', include('sysimibio.imibio_tree_ecological_data.urls')), # todo cambiar a ingles
    path('bioblitz/', include('sysimibio.bioblitz.urls')),
    path('mapa/', TemplateView.as_view(template_name='tree_map.html'), name='map'), # todo cambiar a ingles
    path('geojson/', v.trees_geojson, name='data'),
    path('publications/', include('sysimibio.bibliography.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
