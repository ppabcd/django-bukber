from admin_totals.admin import ModelAdminTotals
from django.contrib import admin
from django.db.models import Sum
from django.db.models.functions import Coalesce

from .models import Kelas, Peserta
# Register your models here.


class PesertaAdmin(ModelAdminTotals):
    exclude = ['created_at', 'updated_at']
    list_display = [
        'nama',
        'kelas',
        'nominal',
        'created_at',
        'updated_at'
    ]
    list_totals = [('nominal', lambda field: Coalesce(Sum(field), 0))]
    list_filter = ['created_at']
    search_fields = ['nama']


class KelasAdmin(admin.ModelAdmin):
    exclude = ['created_at', 'updated_at', 'user']

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


admin.site.register(Peserta, PesertaAdmin)
admin.site.register(Kelas, KelasAdmin)
