from django.contrib import admin
from .models import CompanyModel, CompanyHomepageURLModel, EsModel

# Register your models here.
admin.site.register(CompanyModel)
admin.site.register(CompanyHomepageURLModel)
admin.site.register(EsModel)