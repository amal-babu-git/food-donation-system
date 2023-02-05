from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):

    def create_superuser(self, email, full_name, password=None, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, full_name, password, **other_fields)

    def create_user(self, email, full_name, password=None, **other_fields):
        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, **other_fields)
        user.set_password(password)
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_DONAR = 'D'
    USER_TYPE_AGENT = 'A'
    USER_TYPE_ADMIN = 'AD'

    USER_TYPE_CHOICES = [
        (USER_TYPE_DONAR, 'Donar'),
        (USER_TYPE_AGENT, 'Agent'),
        (USER_TYPE_ADMIN, 'Admin'),
    ]

    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=12, unique=True, blank=True, null=True)
    full_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    user_type = models.CharField(
        max_length=2, choices=USER_TYPE_CHOICES, default=USER_TYPE_DONAR)
    start_date = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS: list[str] = ['full_name', 'user_type']

    def __str__(self) -> str:
        return self.email
    pass
