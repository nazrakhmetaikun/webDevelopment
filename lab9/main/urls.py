from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path("companies/",views.list_companies),
    path('companies/<int:id>',views.onecompany),
    path('companies/<int:id>/vacancies',views.list_vacancies_of_company),
    path('vacancies/',views.list_vacancies),
    path('vacancies/<int:id>',views.onevacancy),
    path('vacancies/top_ten',views.top_vacancies)
]
