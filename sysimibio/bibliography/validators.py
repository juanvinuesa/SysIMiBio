from django.core.exceptions import ValidationError


def validate_isbn(isbn):
    if len(isbn) != 10 and len(isbn) != 13:
        raise ValidationError("Ingrese un ISBN con 10 o 13 caracteres")
