from django.shortcuts import render
from django.http import JsonResponse
from .models import Company,Vacancies
# Create your views here.
def list_companies(request):
    companies = list(Company.objects.values())
    print(companies)
    return JsonResponse(companies,safe=False)

def onecompany(request,id):
    company = list(Company.objects.filter(id=id).values())
    return JsonResponse(company,safe=False)

def list_vacancies_of_company(request,id):
    company = Company.objects.get(id=id)
    vacancies = list(company.vacancies.values())
    return JsonResponse(vacancies,safe=False)

def list_vacancies(request):
    vacancies = list(Vacancies.objects.values())
    return JsonResponse(vacancies,safe=False)

def onevacancy(request,id):
    vacancy = list(Vacancies.objects.filter(id=id).values())
    return JsonResponse(vacancy,safe=False)

def top_vacancies(request):
    vacancies = list(Vacancies.objects.order_by('salary')[:10].values())
    return JsonResponse(vacancies,safe=False)