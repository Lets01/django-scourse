# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def curso_list(request):
    return render(request, 'curso_list.html')

def curso(request):
    return render(request, 'curso.html')