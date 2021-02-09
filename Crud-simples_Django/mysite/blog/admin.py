from django.contrib import admin

from .models import Carros


class CarrosAdmin(admin.ModelAdmin):
    list_display = ('modelo','marca','ano')


admin.site.register(Carros,CarrosAdmin)
