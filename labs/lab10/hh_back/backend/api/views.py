from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from .models import Company, Vacancy
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    return HttpResponse("Home Page")

@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        company = Company.objects.all()
        data = {'products': list(company.values())}
        return JsonResponse(data)
    elif request.method == 'POST':
        data = json.loads(request.body)
        company = Company.objects.create(name=data.get("name"))

        return JsonResponse({'message': 'Company created successfully'}, status=201)

@csrf_exempt
def company_by_id(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse(data={"error": str(e)}, status = 400)


    if request.method == 'GET':
        data = {'company': {
            'id': company.id,
            'name': company.name,
            'description': company.description,
            'city': company.city,
            'address': company.address
        }}
        return JsonResponse(data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        company.name = data.get("name")
        company.save()
        return JsonResponse(company.to_json())
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({"deleted": True})
    

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
    vacancies = company.vacancies.all()
    data = {'vacancies': list(vacancies.values())}
    return JsonResponse(data)

def top_ten_vacancies(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    data = {'vacancies': list(vacancies.values())}
    return JsonResponse(data)
