from django.contrib import admin

# Register your models here.
from apps.users.models import MainUser

admin.site.register(MainUser)
