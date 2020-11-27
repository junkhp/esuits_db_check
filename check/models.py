from django.db import models

# Create your models here.


class CompanyModel(models.Model):
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class CompanyHomepageURLModel(models.Model):
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    homepage_url = models.URLField(max_length=200)

    def __str__(self):
        return self.homepage_url


class EsModel(models.Model):
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    company_url = models.ForeignKey(CompanyHomepageURLModel, on_delete=models.CASCADE)
    selection_type = models.CharField(max_length=100, null=True, blank=True)
    print(company)

    def __str__(self):
        if self.selection_type is None:
            return self.company.company_name + '_none'
        else:
            return self.company.company_name + '_' + self.selection_type
