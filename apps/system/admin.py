from django.contrib import admin
from apps.system import models


# Register your models here.


@admin.register(models.Version)
class SystemVersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'version', 'activate',
                    'content', 'created_at', 'updated_at')
    ordering = ('-created_at',)
