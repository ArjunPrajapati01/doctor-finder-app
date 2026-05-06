from django.contrib import admin
from .models import Specialization , Doctor
# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name','specialization','exprience_years','location')
    search_fields = ('name','specialization_name','location')

admin.site.register(Specialization)