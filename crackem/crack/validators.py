from django.core.exceptions import ValidationError


def names_with_alphas(value):
    for letter in value:
        if not letter.isalpha():
            raise ValidationError("Name should contain only alphas!")


def password_validator(value):
    alpha_count = 0
    digit_count = 0
    for char in value:
        if char.isalpha():
            alpha_count += 1
        elif char.isdigit():
            digit_count += 1
    if alpha_count == 0:
        raise ValidationError("Password should contain at least one letter")
    if digit_count == 0:
        raise ValidationError("Password should contain at least one digit")
