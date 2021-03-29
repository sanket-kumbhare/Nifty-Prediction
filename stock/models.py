from django.db import models

# Create your models here.


class Companies(models.Model):
    name = models.CharField(max_length=256, blank=True)
    symbol = models.CharField(max_length=256, blank=True)
    industry = models.CharField(max_length=256, blank=True)
    isinCode = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_company_by_id(pk):
        return Companies.objects.get(pk=pk)
