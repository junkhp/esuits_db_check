from django.contrib import admin
from .models import CompanyModel, CompanyHomepageURLModel, EsModel, TagModel, CustomUserModel, QestionModel

# Register your models here.
admin.site.register(CompanyModel)
admin.site.register(CompanyHomepageURLModel)
admin.site.register(EsModel)
admin.site.register(CustomUserModel)
admin.site.register(TagModel)
admin.site.register(QestionModel)
