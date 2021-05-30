from django.db import models

from apps.core import Gender


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(
        "Время создания", auto_now_add=True, db_index=True
    )
    changed_at = models.DateTimeField(
        "Время последнего изменения", auto_now=True, db_index=True
    )

    class Meta:
        abstract = True


class PersonMixin(models.Model):
    class Meta:
        abstract = True

    iin = models.CharField(
        'ИИН',
        max_length=12,
        blank=True, null=True,
        unique=True)
    first_name = models.CharField("Имя", max_length=255, blank=True, default='')
    last_name = models.CharField("Фамилия", max_length=255, blank=True, default='')
    middle_name = models.CharField("Отчество", max_length=255, blank=True, default='')
    birthday = models.DateField('Дата рождения', blank=True, null=True)
    gender = models.CharField('Пол', max_length=10, choices=Gender.choices, blank=True, null=True)