from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("companies/", views.company_list, name = "allCompanies"),
    path("companies/<int:company_id>", views.company_by_id, name = "companyById"),
    path("vacancies/", views.vacancy_list, name = "allvacancies"),
    path("vacancies/<int:vacancy_id>", views.vacancy_by_id, name = "vacancyById"),
    path("companies/<int:company_id>/vacancies", views.company_vacancies, name = "companyVacancies"),
    path('vacancies/top_ten/', views.top_ten_vacancies),
]