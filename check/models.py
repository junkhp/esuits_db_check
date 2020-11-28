# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUserModel(AbstractUser):
    '''カスタムユーザークラス'''
    class Meta(object):
        db_table = 'custom_user'

    def __str__(self):
        return self.username


class TagModel(models.Model):
    tag_name = models.CharField(max_length=50)
    author = models.ManyToManyField(CustomUserModel)

    def __str__(self):
        return self.tag_name


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

    def __str__(self):
        if self.selection_type is None:
            return self.company.company_name + '_none'
        else:
            return self.company.company_name + '_' + self.selection_type


class QestionModel(models.Model):
    es = models.ForeignKey(EsModel, on_delete=models.CASCADE)            
    question = models.TextField()
    tags = models.ManyToManyField(TagModel)

    def __str__(self):
        return self.question
