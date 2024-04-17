from django.contrib import admin
from .models import Vacancy, Company

admin.site.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name')

# Register your models here.
admin.site.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'salary', 'company')
    search_fields = ('name')
