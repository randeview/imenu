from django.db import models

from apps.core.models import TimestampMixin
from apps.users.models import MainUser


class Organization(TimestampMixin):
    name = models.CharField('Наименования организации', max_length=500)
    owner = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='organizations')
    address = models.CharField('Адрес', max_length=999)
    description = models.TextField('Описания ресторана', null=True, blank=True)
    logo = models.ImageField('Логотип', null=True, blank=True)

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'

    def __str__(self):
        return self.name


class Menu(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='menus')

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'
