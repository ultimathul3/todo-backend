from django.contrib import admin
from .models import Todos


class TodosAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'created_at', 'user']


admin.site.register(Todos, TodosAdmin)
