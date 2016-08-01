from __future__ import unicode_literals

from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    ticker = models.CharField(max_length=200, blank=True, unique=True)
    exchange = models.CharField(max_length=200, blank=True)
    industry = models.CharField(max_length=200, blank=True)
    sector = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Keyword(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=500)

    def __str__(self):
        return self.keyword