# Bibliography app
La app `bibliography` hace parte del sistema de gestión de conocimiento del IMIBIO. Está creada para registrar infomraciones a respecto de libros, artículos y otros tipos de publicaciones. Posee la capacidad de resgatar información oficial de las publicaciones que tienen [DOI (Digital Object Identification)](https://www.doi.org/) o [ISBN (International Standard Book)](https://www.isbn.org.ar/). Aquellas publicaciones que no poseen DOI ni ISBN, podrán ser cargadas siendo necesário que el usuário registro todas las informaciones conocidas de manera manual. En dichos casos, **el sistema no aceptará registro de publicaciones sin `título`, `autor` y `año de publicación`.** 

El campo booleano `crossref`, que posee valor por defecto `True` sive para indicar cuando la publicación posee `DOI` o `ISBN`, sendo usada como um indicador del sistema cuando se debe usar las APIs de rescate de metadatos.

Trás el registro de la publicación el usuário podrá editar los campos, cuando le convenga.

## APIs
La app usa API´S de [Crossrefapi](https://www.crossref.org/blog/python-and-ruby-libraries-for-accessing-the-crossref-api/) y [isbnlib](https://pypi.org/project/isbnlib/), para rescatar los metadatos de `DOI` y `ISBN`, respectivamente.
 
### Validadores y limpieza 
* [`validate_isbn`](sysimibio/bibliography/validators.py): Es usado para validar el campo `ISBN`, confirmando que el valor ingresado tenga 10 o 13 dígitos. Caso contrário retorna un `ValidationError`

* En el método [`clean()`](sysimibio/bibliography/forms.py) de `PublicationForm`:
    *  se hace la confirmación de la existencia de un valor de `DOI`, `ISBN` y `crossref` habilitado (`True`). Caso contrário, retorna `ValidationError`.
    * se hace la confirmar ción de la existéncia de valores para `título`, `autor` y `año de publicación` para cuando el `crossref` estes deshabilitado (`False`). Caso contrário, retorna `ValidationError`.
    
* En el método [`clean_ISBN`](sysimibio/bibliography/forms.py) de `PublicationForm`:
    * Se hace un proceso de limpieza de los valores ingresados de `ISBN`:
        * se excluyen los guiones y puntos;
        * se convirte `ISBN` de 10 caracteres para 13, usando `isblib`;
