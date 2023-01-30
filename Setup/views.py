from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from Setup import models
from .forms import *
from Transaction import models as transactionmodel
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    page_title = 'Setup Home Page'
    return render(request, 'home.html', {'page_title': page_title})


def item(request):
    aa = items.objects.all()
    page_title = 'Items Data'
    return render(request, 'item.html', {'data': aa, 'page_title': page_title})


def suppliers(request):
    aa = supplier.objects.all()
    page_title = 'Suppliers Data'
    return render(request, 'supplier.html', {'data': aa, 'page_title': page_title})


def customers(request):
    aa = customer.objects.all()
    page_title = 'Customers Data'
    return render(request, 'customer.html', {'data': aa, 'page_title': page_title})


def storages(request):
    aa = storage.objects.all()
    page_title = 'Storages Data'
    return render(request, 'storage.html', {'data': aa, 'page_title': page_title})


def additem(request):
    page_title = 'Add Item'
    if request.method == 'POST':
        newitem = additemForm(request.POST or None)
        if newitem.is_valid():
            newitem.save()
        return HttpResponseRedirect(reverse('add-item'))
    else:
        newitem = additemForm
    return render(request, 'additems.html', {'page_title':page_title})


def addstorage(request):
    page_title = 'Add Storage'
    if request.method == 'POST':
        newstorage = addstorageForm(request.POST or None)
        if newstorage.is_valid():
            newstorage.save()
        return HttpResponseRedirect(reverse('add-storage'))
    else:
        newstorage = addstorageForm
    return render(request, 'addstorage.html', {'page_title':page_title})


def addcustomer(request):
    page_title = 'Add Customer'
    if request.method == 'POST':
        newcustomer = addcustomerForm(request.POST or None)
        if newcustomer.is_valid():
            newcustomer.save()
        return HttpResponseRedirect(reverse('add-customer'))
    else:
        newcustomer = addcustomerForm
    return render(request, 'addcustomer.html', {'page_title':page_title})


def addsupplier(request):
    page_title = 'Add Supplier'
    if request.method == 'POST':
        newsupplier = addsupplierForm(request.POST or None)
        if newsupplier.is_valid():
            newsupplier.save()
        return HttpResponseRedirect(reverse('add-supplier'))
    else:
        newsupplier = addsupplierForm
        return render(request, 'addsupplier.html', {'page_title':page_title})
