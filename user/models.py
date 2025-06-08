"""from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Profile(AbstractUser):
    email = models.CharField(max_length=133, unique=True)
    cpf = models.CharField(max_length=11)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []"""

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O campo Email é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser precisa ter is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser precisa ter is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class Profile(AbstractUser):
    username = models.CharField(max_length=150, unique=True)  # mantém obrigatório
    email = models.EmailField(_("email address"), unique=True)
    cpf = models.CharField(max_length=11)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # necessário para createsuperuser

    objects = CustomUserManager()

    def __str__(self):
        return self.email
