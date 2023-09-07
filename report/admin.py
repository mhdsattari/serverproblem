from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = '__all__'