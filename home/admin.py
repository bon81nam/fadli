from django.contrib import admin
from .models import InputFormModel


# Register your models here.
class FormAdmin(admin.ModelAdmin):
    list_display = ['JABATAN', 'Tempoh', 'tahun', 'KPI', 'Tajuk_Aktiviti']
    search_fields = ['JABATAN', 'Tempoh', 'tahun', 'KPI']
    list_filter = ['JABATAN', 'tahun', 'KPI']
    list_display = ['JABATAN', 'Tajuk_Aktiviti', 'KPI', 'tahun']
    list_per_page = 8


admin.site.register(InputFormModel, FormAdmin)
