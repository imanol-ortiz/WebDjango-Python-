from django.contrib import admin
from .models import Postmodel
# Register your models here.

class Postmodeladmin(admin.ModelAdmin):
    list_display = ('titulo', 'date_created')
admin.site.register(Postmodel, Postmodeladmin)