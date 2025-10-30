from django.contrib import admin
from .models import Post,Registration 
admin.site.register(Post)
admin.site.register(Registration)  

from django.contrib import admin
from .models import Record

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status', 'created_at')
    readonly_fields = []

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.status == 'published':
            return [field.name for field in self.model._meta.fields if field.name != 'id']
        return self.readonly_fields

    def has_change_permission(self, request, obj=None):
        if obj and obj.status == 'published':
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        return True  # Allow delete for both draft and published