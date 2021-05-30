from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.core.models import TimestampMixin, PersonMixin
from apps.users.managers import UserManager


class MainUser(TimestampMixin, PermissionsMixin, PersonMixin, AbstractBaseUser):
    phone = PhoneNumberField(_('Моб. телефон'), unique=True, null=True, blank=True)
    email = models.EmailField(_('Email'), null=True, blank=True, unique=True)
    is_active = models.BooleanField(_('Активный'), default=True)
    is_staff = models.BooleanField(_('Сотрудник'), default=False)
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
