from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from .models import Company, Vacancy


# Create your views here.
def home(request):
    return HttpResponse("Home Page")

def company_list(request):
    company = Company.objects.all()
    data = {'products': list(company.values())}
    return JsonResponse(data)

def company_by_id(request, company_id):
    company = get_object_or_404(Company, id = company_id)
    data = {'company': {
        'id': company.id,
        'name': company.name,
        'description': company.description,
        'city': company.city,
        'address': company.address
    }}
    return JsonResponse(data)

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    data = {'categories': list(vacancies.values())}
    return JsonResponse(data)

def vacancy_by_id(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, id = vacancy_id)
    data = {'vacancy': {
        "id": vacancy.id,
        "name": vacancy.name
    }}
    return JsonResponse(data)

def company_vacancies(request, company_id):
    company = get_object_or_404(Company, id = company_id)
    vacancies = company.product_set.all()
    data = {'vacancies': list(vacancies.values())}
    return JsonResponse(data)

def top_ten_vacancies(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    data = {'vacancies': list(vacancies.values())}
    return JsonResponse(data)
