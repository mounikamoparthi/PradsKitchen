# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from ..recipe.models import Recipes, Mix, Category
import json
import re


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
    print("keys"*10)
    new_cat=request.POST['new_category']
    catID=None
    # Checking and creating Id (Retrieving Category Id)

    if (len(new_cat)!=0):
        f=Category.objects.filter(CategoryName =new_cat)
        if (len(f)==0):
            Category.objects.create(CategoryName=new_cat)
            catID=Category.objects.latest('id')
        else:
            print("Cat Id"*100)
            print f
            catID=f[0]['id']

    # Grabbing list of ingredients
    List_of_quantity=[]
    List_of_ingredients=[]
    for key in request.POST:
        if (re.match(r'[ing]',key)):
            print "brook"
            List_of_ingredients.append(request.POST[key])
        if (re.match(r'[qty]',key)):
            print "Monica"
            List_of_quantity.append(request.POST[key])

    # Seperating inputs for RecipeManager
    I_data={
        "DishName": str(request.POST['DishName']),
        "Procedure": str(request.POST['Procedure']),
        "CookTime":  str(request.POST['CookTime']),
        "YoutubeLink":  str(request.POST['YoutubeLink']),
    }

    # iresults=Ingredients.objects.check_ingredient(List_of_ingredients)
    # if (iresults['status']):
    #     for k in List_of_ingredients:
    #         Ingredients.objects.create(Name=k)


    results=Recipes.objects.check_recipe(I_data)
    if (results['status']):
        Recipes.objects.create(DishName=I_data['DishName'],Procedure=I_data['Procedure'],CookTime=I_data['CookTime'],YoutubeLink=I_data['YoutubeLink'],CategoryId=catID)
        return redirect(reverse('recipe:show_path'))
    else:
        context={
            'errors': results['errors'],
            'categories': Category.objects.all(),
        }
        return render(request, 'recipeadmin/newrecipe.html', context)
    return redirect(reverse ('recipe:index_path'))
