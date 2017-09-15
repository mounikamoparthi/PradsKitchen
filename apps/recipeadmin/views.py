# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from ..recipe.models import Recipes,Ingredients, Mix, Category
import json
from django.core import serializers

# Create your views here.
def login(request):
    return render(request, 'recipeadmin/login.html')

def new(request):
    print request.POST['email']
    i = Ingredients.objects.all()
    si = serializers.serialize("json", i, fields = ('id', 'Name'))
    context = {
        'categories': Category.objects.all(),
        'ingredients': i,
        'serializeding': si

    }
    return render(request, 'recipeadmin/newrecipe.html', context)

def create(request):
    print (request.POST)
    return redirect(reverse ('recipe:index_path'))
