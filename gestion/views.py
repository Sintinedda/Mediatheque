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
            errmsg = 'Cette catégorie existe déjà!!!'
            return render(request, 'category/addcat.html',
                          {'form': form, 'errmsg': errmsg})
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
            errmsg = 'Cette catégorie existe déjà!!!'
            return render(request, 'category/editcat.html',
                          {'form': form, 'errmsg': errmsg, 'cat': cat})
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
            errmsg = 'Cet item existe dejà!!!'
            return render(request, 'item/additem.html',
                          {'form': form, 'errmsg': errmsg, 'cat': cat})
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
            errmsg = 'Cet item existe déjà!!!'
            return render(request, 'item/edititem.html',
                          {'form': form, 'errmsg': errmsg, 'cat': cat, 'item': item})
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


                                               # MEMBER

def memblist(request):
    members = Member.objects.all()
    return render(request, 'member/memblist.html',
                  {'members': members})

def addmemb(request):
    if request.method == 'POST':
        form = AddMemberForm(request.POST)
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        if Member.objects.filter(firstname=firstname, lastname=lastname).exists():
            errmsg = "Ce membre existe déjà!!!"
            return render(request, 'member/addmemb.html',
                          {'form': form, 'errmsg': errmsg})
        else:
            if form.is_valid():
                memb = Member()
                memb.firstname = form.cleaned_data['firstname']
                memb.lastname = form.cleaned_data['lastname']
                memb.save()
                return redirect('memblist')
    else:
        form = AddMemberForm()
        return render(request, 'member/addmemb.html',
                      {'form': form})


def editmemb(request, id):
    memb = Member.objects.get(pk=id)
    if request.method == 'POST':
        form = EditMemberForm(request.POST)
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        if Member.objects.filter(firstname=firstname, lastname=lastname).exists():
            name = memb.firstname + ' ' + memb.lastname
            errmsg = "Ce membre existe déjà!!!"
            return render(request, 'member/editmemb.html',
                          {'form': form, 'errmsg': errmsg, 'name': name})
        else:
            if form.is_valid():
                memb.firstname = form.cleaned_data['firstname']
                memb.lastname = form.cleaned_data['lastname']
                memb.save()
                return redirect('memblist')
    else:
        form = EditMemberForm()
        name = memb.firstname + ' ' + memb.lastname
        return render(request, 'member/editmemb.html',
                      {'form': form, 'name': name})


def delmemb(request, id):
    memb = Member.objects.get(pk=id)
    if request.method == 'POST':
        memb.delete()
        return redirect('memblist')
    else:
        name = memb.firstname + ' ' + memb.lastname
        return render(request, 'member/delmemb.html',
                      {'name': name})


def cardmemb(request, id):
    memb = Member.objects.get(pk=id)
    loans = Loan.objects.filter(member=memb.pk)
    if memb.blocked:
        if request.method == 'POST':
            memb.blocked = False
            memb.save()
            return render(request, 'member/cardmemb.html',
                          {'memb': memb, 'loans': loans})
        else:
            return render(request, 'member/cardmemb.html',
                          {'memb': memb, 'loans': loans})
    else:
        if request.method == 'POST':
            memb.blocked = True
            memb.save()
            return render(request, 'member/cardmemb.html'
                          ,{'memb': memb, 'loans': loans})
        else:
            return render(request, 'member/cardmemb.html',
                          {'memb': memb, 'loans': loans})