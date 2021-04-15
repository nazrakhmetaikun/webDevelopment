from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50,verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    city = models.CharField(max_length=20,verbose_name="Город")
    address = models.TextField(verbose_name="Местонахождение")

    def __str__(self):
        return "{}".format(self.name)
    

class Vacancies(models.Model):
    name = models.CharField(max_length=50,verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    salary = models.FloatField(verbose_name="Зарплата")
    company = models.ForeignKey(Company,related_name="vacancies",on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)

    