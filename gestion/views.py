from dbm.sqlite3 import error

from django.shortcuts import render, redirect
from .models import *
from .forms import *


                                             # CATEGORY

def catlist(request):
    categories = Category.objects.all()
    return render(request, 'category/catlist.html',
                  {'categories': categories})


def addcat(request):
    if request.method == 'POST':
        form = AddCatForm(request.POST)
        name = request.POST.get('name')
        if Category.objects.filter(name=name).exists():
            error = 'Cette catégorie existe déjà!!!'
            return render(request, 'category/addcat.html',
                          {'form': form, 'error': error})
        else:
            if form.is_valid():
                cat = Category()
                cat.name = form.cleaned_data['name']
                cat.save()
                return redirect('catlist')
    else:
        form = AddCatForm()
        return render(request, 'category/addcat.html',
                      {'form': form})


def editcat(request, cat):
    cat = Category.objects.get(name=cat)
    if request.method == 'POST':
        form = EditCatForm(request.POST)
        name = request.POST.get('name')
        if Category.objects.filter(name=name).exists():
            error = 'Cette catégorie existe déjà!!!'
            return render(request, 'category/editcat.html',
                          {'form': form, 'error': error, cat: cat})
        else:
            if form.is_valid():
                cat.name = form.cleaned_data['name']
                cat.save()
                return redirect('catlist')
    else:
        form = EditCatForm()
        return render(request, 'category/editcat.html',
                      {'form': form, 'cat': cat})


def delcat(request, cat):
    cat = Category.objects.get(name=cat)
    if request.method == 'POST':
        cat.delete()
        return redirect('catlist')
    else:
        return render(request, 'category/delcat.html',
                      {'cat': cat})