from django.contrib import admin

# Register your models here.

from .models import CardTask


class CardTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_start', 'time_end', 'time_end', 'task_status', )
    list_display_links = ('title', )
    search_fields = ('title', 'task_status')
    list_filter = ('time_start',)


admin.site.register(CardTask, CardTaskAdmin)
