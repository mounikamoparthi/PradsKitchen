# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from ..recipe.models import Recipes,Ingredients, Mix, Category
import json


# Create your views here.
def login(request):
    return render(request, 'recipeadmin/login.html')

def new(request):
    print request.POST['email']

    context = {
        'categories': Category.objects.all(),

    }
    return render(request, 'recipeadmin/newrecipe.html', context)

def create(request):
    print("*"*100)
    print (type(request.POST["DishName"]))
    I_data={
        "DishName": str(request.POST['DishName']),
        "Procedure": str(request.POST['Procedure']),
        "CookTime":  str(request.POST['CookTime']),
        "YoutubeLink":  str(request.POST['YoutubeLink']),
    }
    results=Recipes.objects.check_recipe(I_data)
    if (results['status']):
        Recipes.objects.create(DishName=I_data['DishName'],Procedure=I_data['Procedure'],CookTime=I_data['CookTime'],YoutubeLink=I_data['YoutubeLink'])
        return redirect(reverse('recipe:show_path'))
    else:
        context={
            'errors': results['errors'],
            'categories': Category.objects.all(),
        }
        return render(request, 'recipeadmin/newrecipe.html', context)
    return redirect(reverse ('recipe:index_path'))
