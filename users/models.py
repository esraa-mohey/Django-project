from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from nationality.models import Nationality
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
# Create your models here.


class Country(models.Model):
    name = models.JSONField(null=False)
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE)

    class Meta:
        db_table = "Country"

    def __str__(self):
        return self.name


class TypeofAccount(models.Model):
    name = models.JSONField(null=False)

    class Meta:
        db_table = "TypeofAccount"

    def __str__(self):
        return self.name


class Type_of_identification(models.Model):
    name = models.JSONField(null=False)

    class Meta:
        db_table = "TypeOfIdentification"

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email,and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        try:

            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user
        except:
            raise

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    """

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    middle_Name = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    date_of_Birth = models.DateField(null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    typeofidentification = models.ForeignKey(
        Type_of_identification, on_delete=models.CASCADE)
    Number_of_identification = models.CharField(
        max_length=30, blank=True, unique=True)
    Home_address = models.CharField(max_length=45, blank=True, null=True)
    typeOfAccount = models.ForeignKey(TypeofAccount, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=30, blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self


class company_info(models.Model):
    name = models.JSONField(null=False)
    deposit = models.FloatField(default=0)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "company_info"
