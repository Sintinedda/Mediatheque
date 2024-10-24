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


                                           # ITEM

def itemlist(request, cat):
    cat = Category.objects.get(name=cat)
    items = Item.objects.filter(category__name=cat)
    loans = Loan.objects.all()
    return render(request, 'item/itemlist.html',
                  {'cat': cat, 'items': items, 'loans': loans})


def additem(request, cat):
    cat = Category.objects.get(name=cat)
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        name = request.POST.get('name')
        creator = request.POST.get('creator')
        if Item.objects.filter(name=name, creator=creator).exists():
            error = 'Cet item existe dejà!!!'
            return render(request, 'item/additem.html',
                          {'form': form, 'error': error, 'cat': cat})
        else:
            if form.is_valid():
                item = Item()
                item.name = form.cleaned_data['name']
                item.creator = form.cleaned_data['creator']
                item.category = Category.objects.get(name=cat)
                item.save()
                return redirect('itemlist', cat)
    else:
        form = AddItemForm()
        return render(request, 'item/additem.html',
                      {'form': form, 'cat': cat})


def edititem(request, cat, id):
    cat = Category.objects.get(name=cat)
    item = Item.objects.get(pk=id)
    if request.method == 'POST':
        form = EditItemForm(request.POST)
        name = request.POST.get('name')
        creator = request.POST.get('creator')
        if Item.objects.filter(name=name, creator=creator).exists():
            error = 'Cet item existe déjà!!!'
            return render(request, 'item/edititem.html',
                          {'form': form, 'error': error, 'cat': cat, 'item': item})
        else:
            if form.is_valid():
                item.name = form.cleaned_data['name']
                item.creator = form.cleaned_data['creator']
                item.category = form.cleaned_data['category']
                item.save()
                return redirect('itemlist', cat)
    else:
        form = EditItemForm()
        return render(request, 'item/edititem.html',
                      {'form': form, 'cat': cat, 'item': item})


def delitem(request, cat, id):
    cat = Category.objects.get(name=cat)
    item = Item.objects.get(pk=id)
    if request.method == 'POST':
        item.delete()
        return redirect('itemlist', cat)
    else:
        return render(request, 'item/delitem.html',
                      {'cat': cat, 'item': item})