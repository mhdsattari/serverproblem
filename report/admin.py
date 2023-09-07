from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = '__all__'

admin.site.register(models.Problem)    
class ProblemAdmin(admin.ModelAdmin):
    list_display = '__all__'
    inlines = 'models.Server'
