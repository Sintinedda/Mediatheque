from django.db import models


class Media(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name


class Borrower(models.Model):
    name = models.CharField(max_length=150)
    blocked = models.BooleanField(default=False)
    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Media, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    loandate = models.DateField()
    available = models.BooleanField(default=True)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    def __str__(self):
        return self.name + ' par ' + self.author