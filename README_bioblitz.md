# Bioblitz app
La app `bioblitz` hace parte del sistema de gestión de datos de biodiversidad del IMIBIO. Está creada para rescatas datos e informaciones al respecto de las actividades de bioblitz desarrolladas por la institución utilizando los servicios de [INaturalist](https://www.inaturalist.org).

Para pode acceder al las informaciones del proyecto bien como las observaciones relacionadas a los mismos, se hace uso de `slug` o`project_id` del proyecto.

La app tiene una pagina de estadísticas representando un resumen al respecto del proyecto en forma de gráficos usando [`chartjs`](https://www.chartjs.org/). Aunque exista el módulo python. Por el momento se está usando su versión SDN.

## APIs
La app usa API [pyinaturalist](https://pypi.org/project/pyinaturalist/) que nos permite regatar tanto informaciión al respecto de proyectos de bioblitz, como las observaciones cargadas para los mismos. Más al respecto de la api:

* [read the doc](https://pyinaturalist.readthedocs.io/en/v0.13.0/)
* [API Reference](https://www.inaturalist.org/pages/api+reference)
 
### Validadores y limpieza 
* En el método [`clean()`](sysimibio/bioblitz/forms.py) de `BioblitzModelForm`:
    *  se hace la confirmación de la existencia de un valor de `slug` o `project_id` del proyecto. Caso contrário, retorna `ValidationError`.

## Base de datos  
![](extras/img/modeldb_app_bioblitz.png)  
