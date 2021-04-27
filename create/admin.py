from django.contrib import admin
from .models import Lounge
class LoungeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
admin.site.register(Lounge,LoungeAdmin)
