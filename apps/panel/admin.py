from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.utils.translation import gettext_lazy as _

import environ

from apps.reuse.class_view import Pagination

env = environ.Env()


@admin.register(LogEntry)
class LogEntryPanelFilter(admin.ModelAdmin, Pagination):
    search_fields = ['object_repr']
    filter_horizontal = ()
    fieldsets = ()
    list_per_page = 25

    def has_add_permission(self, request):
        return False

    def change_view(self, request, object_id, extra_context=None):
        """ customize add/edit form """
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(LogEntryPanelFilter, self).change_view(request, object_id, extra_context=extra_context)

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        pass

    def delete_model(self, request, obj):
        pass

    def save_related(self, request, form, formsets, change):
        pass


admin.site.site_header = env("SITIOWEB", default=_('AirBNB Cuba'))
admin.site.site_title = env("PORTAL", default=_('AirBNB Cuba'))
admin.site.index_title = env("BIENVENIDOS", default=_('Bienvenidos al portal de administración AirBnB Cuba'))
