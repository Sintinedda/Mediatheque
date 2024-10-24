import datetime
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    blocked = models.BooleanField(default=False)

    def __str__(self):
        name = f'{self.firstname} {self.lastname}'
        return name

    class Meta:
        ordering = ['lastname', 'firstname']
        unique_together = ('firstname', 'lastname')


class Item(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        unique_together = ('name', 'creator')


class Loan(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f'{self.member} {self.item} {self.date}'

    class Meta:
        unique_together = ('member', 'item', 'date')