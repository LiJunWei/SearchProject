#coding:utf-8
from django.db import models


class Results(models.Model):
    content = models.CharField(max_length=50)
    def __str__(self):
        return self.content