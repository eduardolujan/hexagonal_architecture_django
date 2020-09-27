from django.contrib import admin

from ..forms import form

class ModelAdmin(admin.ModelAdmin):
    form = form

