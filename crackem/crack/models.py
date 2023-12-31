from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator
from django.db import models


from crackem.crack.validators import names_with_alphas


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=20, validators=[
        MinLengthValidator(2, 'Name cannot be less than 2 characters!'),
        MaxLengthValidator(20, 'Name cannot exceeds 20 characters!'),
        names_with_alphas], blank=False, null=False)
    last_name = models.CharField(max_length=20,
                                 validators=[MinLengthValidator(2, 'Name cannot be less than 2 characters!'),
                                             MaxLengthValidator(20, 'Name cannot exceeds 20 characters!'),
                                             names_with_alphas], blank=False, null=False)

    username = models.CharField(max_length=20, unique=True, blank=False, null=False,
                                validators=[MinLengthValidator(2, 'Name cannot be less than 2 characters!'),
                                            MaxLengthValidator(20, 'Name cannot exceeds 20 characters!')])

    password = models.CharField(max_length=20, blank=False, null=False,
                                validators=[MinLengthValidator(6, 'Password cannot be less than 6 characters'),
                                            MaxLengthValidator(20, 'password cannot be more than 10 characters')])
    email = models.EmailField(unique=True, validators=[EmailValidator(message='Enter a valid email address.')])
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password', 'email']
    USERNAME_FIELD = 'username'


