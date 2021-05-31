from django.db.models import TextChoices


class Roles(TextChoices):
    OWNER = "OWNER", "Владелец"
    CLIENT = "CLIENT", "Клиент"
