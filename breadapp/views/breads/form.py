import sqlite3
from django.shortcuts import render, redirect, reverse
from breadapp.views.breads.list import bread_list

def bread_form(request): 
    if request.method == 'GET': 
        template = 'breads/form.html'
        context = {}
        return render(request, template, context)