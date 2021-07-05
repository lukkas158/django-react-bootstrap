from base.models import Timestamp
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, name,  date_of_birth, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not name:
            raise ValueError("User must have a full name")
        if not date_of_birth:
            raise ValueError("User must have a full name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.name = name
        user.set_password(password)
        user.date_of_birth = date_of_birth
        user.active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name,  date_of_birth, password=None, **extra_fields):
        user = self.create_user(
            email, name, date_of_birth, password, **extra_fields)

        user.is_admin = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, Timestamp):

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    # Passwords can be null if the user has logged
    # from Social Auth.
    password = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'date_of_birth']

    objects = UserManager()

    # Theses fields are necessary in order to be compliant with the django admin.
    def __str__(self) -> str:
        return f"{ self.email}  -  {self.name}"

    def has_perm(self, perm, obj=None) -> bool:
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label) -> bool:
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
