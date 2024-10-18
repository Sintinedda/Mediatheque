from django.shortcuts import render, redirect
from django.utils.functional import empty

from .forms import *
from .models import *


# MEDIAS

def listmedia(request):
    medias = Media.objects.all()
    return render(request, 'medias/listmedia.html',
                  {'medias': medias})


def addmedia(request):
    if request.method == 'POST':
        form = AddMediaForm(request.POST, request.FILES)
        form.name = request.POST.get('name')
        if Media.objects.filter(name=form.name).exists():
            error = 'Cette catégorie existe déjà!!!'
            return render(request, 'medias/addmedia.html',
                          {'form': form, 'error': error})
        else:
            if form.is_valid():
                media = Media()
                media.name = form.cleaned_data['name']
                media.save()
                return redirect('listmedia')
    else:
        form = AddMediaForm()
        return render(request, 'medias/addmedia.html',
                      {'form': form})


def updatemedia(request, cat):
    if request.method == 'POST':
        media = Media.objects.get(name=cat)
        form = UpdateMediaForm(request.POST, request.FILES)
        if form.is_valid():
            media.name = form.cleaned_data['name']
            media.save()
            return redirect('listmedia')
    else:
        form = UpdateMediaForm()
        return render(request, 'medias/updatemedia.html',
                      {'form': form})


def deletemedia(request, cat):
    media = Media.objects.get(name=cat)
    if request.method == 'POST':
        media.delete()
        return redirect('listmedia')
    else:
        return render(request, 'medias/deletemedia.html',
                      {'media': media})


# Items

def listitem(request, cat):
    media = Media.objects.get(name=cat)
    items = Item.objects.filter(category__name=cat)
    return render(request, 'items/listitem.html',
                  {'items': items, 'media': media})


def additem(request, cat):
    media = Media.objects.get(name=cat)
    if request.method == 'POST':
        form = AddItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = Item()
            item.name = form.cleaned_data['name']
            item.author = form.cleaned_data['author']
            item.category = Media.objects.get(pk=media.id)
            item.save()
            return redirect('listitem', cat)
    else:
        form = AddItemForm()
        return render(request, 'items/additem.html',
                      {'form': form, 'media': media})


def updateitem(request, cat, id):
    media = Media.objects.get(name=cat)
    if request.method == 'POST':
        item = Item.objects.get(pk=id)
        form = UpdateItemForm(request.POST, request.FILES)
        if form.is_valid():
            item.name = form.cleaned_data['name']
            item.author = form.cleaned_data['author']
            item.category = form.cleaned_data['category']
            item.save()
            return redirect('listitem', cat)
    else:
        form = UpdateItemForm()
        return render(request, 'items/updateitem.html',
                        {'form': form, 'media': media})


def deleteitem(request, cat, id):
    media = Media.objects.get(name=cat)
    item = Item.objects.get(pk=id)
    if request.method == 'POST':
        item.delete()
        return redirect('listitem', cat)
    else:
        return render(request, 'items/deleteitem.html',
                      {'item': item, 'media': media})


def lenditem(request, cat, id):
    media = Media.objects.get(name=cat)
    item = Item.objects.get(pk=id)
    if item.available:
        if request.method == 'POST':
            form = LendItemForm(request.POST, request.FILES)
            if form.is_valid():
                item.borrower = form.cleaned_data['membre']
                item.available = False
                item.save()
                return redirect('listitem', cat)
        else:
            form = LendItemForm()
            return render(request, 'items/lenditem.html',
                          {'item': item, 'form': form, 'media': media})
    else:
        if request.method == 'POST':
                item.available = True
                item.borrower = None
                item.save()
                return redirect('listitem', cat)
        else:
            borrower = item.borrower
            return render(request, 'items/returnitem.html',
                          {'item': item, 'media': media, 'borrower': borrower})