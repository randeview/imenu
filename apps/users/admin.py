from django.contrib import admin

# Register your models here.
from apps.users.models import MainUser, Role

admin.site.register(MainUser)
admin.site.register(Role)
