from django.contrib import admin

from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display=(
        "id","title","is_completed","owner_id","created_at"
    )

admin.site.register(Task, TaskAdmin)