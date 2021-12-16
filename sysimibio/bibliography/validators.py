from django.core.exceptions import ValidationError


def validate_isbn(isbn):
    if len(isbn) != 10 and len(isbn) != 13:
        raise ValidationError("Ingrese un ISBN con 10 o 13 caracteres")


def validate_doi_prefix(doi):
    if not doi.startswith("10."):
        raise ValidationError("Doi tiene que comenzar con 10.")


def validate_doi_slash(doi):
    if not doi.find("/") > 4:
        raise ValidationError("Doi tiene que tener / a partir del cuarto caracter")
