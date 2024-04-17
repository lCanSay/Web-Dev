from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    city = models.CharField(max_length = 255)
    address = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name
        }
    
class Vacancy(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    salary = models.FloatField()
    company  = models.ForeignKey(
        Company, 
        on_delete = models.CASCADE,
        related_name="vacancies")

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"

    def __str__(self):
        return self.name