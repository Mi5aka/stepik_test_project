from django.contrib import admin

from .models import Decision


class DecisionAdmin(admin.ModelAdmin):
    model = Decision
    readonly_fields = []
    list_filter = ('status', 'created_at')
    list_display = ('id', 'status', 'created_at')

    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
               [field.name for field in obj._meta.fields] + \
               [field.name for field in obj._meta.many_to_many]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Decision, DecisionAdmin)
