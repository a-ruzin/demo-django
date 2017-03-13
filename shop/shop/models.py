from datetime import timedelta

from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    price = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    in_stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date added', auto_now_add=True)

    def __str__(self):
        return "{} ({})".format(self.title, self.price)

    def is_new(self):
        return self.pub_date > timezone.now() - timedelta(days=1)
