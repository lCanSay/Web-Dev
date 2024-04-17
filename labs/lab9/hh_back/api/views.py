from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from .models import Company, Vacancy


companies = [
    {"id": 1, "name": "Google", "description": "Description 1", "city": "Almaty", "address": "Abay str 168"},
    {"id": 2, "name": "BI group", "description": "Description 2", "city": "Astana", "address": "Gagarin str 16"},
    {"id": 3, "name": "Samsung", "description": "Description 2", "city": "Shymkent", "address": "Timiryzeva 45"}
]

vacancies = [
    {"id": 1, "name": "Software Engineer", "description": "Description 1", "salary": 100000, "company": 1},
    {"id": 2, "name": "Data Scientist", "description": "Description 2", "salary": 120000, "company": 1},
    {"id": 3, "name": "Web Developer", "description": "Description 3", "salary": 90000, "company": 2},
    {"id": 4, "name": "UX Designer", "description": "Description 4", "salary": 95000, "company": 2},
    {"id": 5, "name": "Product Manager", "description": "Description 5", "salary": 110000, "company": 3},
    {"id": 6, "name": "QA Engineer", "description": "Description 6", "salary": 85000, "company": 3},
    {"id": 7, "name": "Business Analyst", "description": "Description 7", "salary": 105000, "company": 1},
    {"id": 8, "name": "Systems Administrator", "description": "Description 8", "salary": 95000, "company": 2},
    {"id": 9, "name": "Network Engineer", "description": "Description 9", "salary": 90000, "company": 2},
    {"id": 10, "name": "DevOps Engineer", "description": "Description 10", "salary": 110000, "company": 3},
    {"id": 11, "name": "Database Administrator", "description": "Description 11", "salary": 85000, "company": 3},
    {"id": 12, "name": "Technical Support Specialist", "description": "Description 12", "salary": 95000, "company": 1},
    {"id": 13, "name": "Security Analyst", "description": "Description 13", "salary": 90000, "company": 2},
    {"id": 14, "name": "Data Analyst", "description": "Description 14", "salary": 105000, "company": 1},
    {"id": 15, "name": "Software Developer", "description": "Description 15", "salary": 100000, "company": 2}
]

# Create your views here.
def home(request):
    return HttpResponse("Home Page")

def company_list(request):
    #company = Company.objects.all()
    data = {'companies': companies}
    return JsonResponse(data)

def company_by_id(request, company_id):
    #company = get_object_or_404(Company, id = company_id)
    company = next((c for c in companies if c["id"] == company_id), None)

    if company:
        data = {'company': {
        'id': company["id"],
        'name': company["name"],
        'description': company["description"],
        'city': company["city"],
        'address': company["address"]
    }}
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Company not found'}, status=404)

def vacancy_list(request):
    #vacancies = Vacancy.objects.all()
    data = {'vacancies': vacancies}
    return JsonResponse(data)

def vacancy_by_id(request, vacancy_id):
    vacancy = next((v for v in vacancies if v["id"] == vacancy_id), None)

    if vacancy:
        data = {'company': {
        'id': vacancy["id"],
        'name': vacancy["name"],
        'salary': vacancy["salary"],
        'company_id': vacancy["company"]
    }}
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Company not found'}, status=404)

def company_vacancies(request, company_id):
    company_vacancies = [vacancy for vacancy in vacancies if vacancy["company"] == company_id]
    data = {'vacancies': company_vacancies}
    return JsonResponse(data)

def top_ten_vacancies(request):
    sorted_vacancies = sorted(vacancies, key=lambda x: x["salary"], reverse=True)
    top_ten = sorted_vacancies[:10]
    data = {'vacancies': top_ten}
    return JsonResponse(data)
