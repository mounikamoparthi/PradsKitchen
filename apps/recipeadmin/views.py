# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User
from ..recipe.models import Recipes, Mix, Category
import json
import re
from django.core.files.storage import FileSystemStorage
import requests

def index(request):
    # r=requests.get("https://www.googleapis.com/auth/youtube.readonly")
    # context={
    #     'r':r.json()
    # }
    # print(context['r'])
    return render(request,'recipeadmin/login.html')

# Create your views here.
def login(request):
    # result = User.objects.loginval(request.POST)
    # if not result['status']:
    #     for error in result['errors']:
    #         messages.error(request,error)
    #     return redirect(reverse('recipeadmin:index_path'))
    # else:
    #     # messages.success(request,"Successful")
    #     request.session['emailid'] = result['user'].emailid
    #     request.session['first_name'] = result['user'].first_name
    #     request.session['user_id'] = result['user'].id
    #     print result['user'].emailid
    #     status="loggedin"
        return redirect(reverse('recipeadmin:new_path'))


def registration(request):
    if not 'user_id' in request.session:
        return redirect(reverse('recipeadmin:index_path'))
    return render(request,'recipeadmin/register.html')

def reg(request):
    print request.POST
    result = User.objects.register(request.POST)
    if not result['status']:
            context={
                    'errors': result['errors'],
                }
        
            return render(request, 'recipeadmin/register.html', context)
            # return redirect(reverse('recipeadmin:register_path'))
    else:
        request.session['emailid'] = result['user'].emailid
        request.session['user_id'] = result['user'].id
        return redirect(reverse('recipeadmin:new_path'))

def edit(request):
    if not 'user_id' in request.session:
        return redirect(reverse('recipeadmin:index_path'))
    context = {
        'users': User.objects.all()
    }
    return render(request,'recipeadmin/editadmin.html', context)

def deleteuser(request,id):
    user1=User.objects.get(id=request.session["user_id"])
    user1.remove()
    return redirect(reverse('recipeadmin:editadmin_path'))


def new(request):
    # if not 'user_id' in request.session:
    #     return redirect(reverse('recipeadmin:index_path'))
    context = {
            'categories': Category.objects.all(),
        }
    return render(request, 'recipeadmin/newrecipe.html', context)

def create(request):
    # print (request)
    # if not 'user_id' in request.session:
    #     return redirect(reverse('recipeadmin:index_path'))
    new_cat=request.POST['new_category']
    catID=None
    # Checking and creating Id (Retrieving Category Id)
    print (request.FILES['foodimg'])
    if((len(new_cat)==0) and (len(request.POST['Category']))==0):
        context={
            'errors': ["Please name the category of the recipe"],
            'categories': Category.objects.all(),
        }
        return render(request, 'recipeadmin/newrecipe.html', context)
    if (len(new_cat)!=0):
        f=Category.objects.filter(CategoryName =new_cat)
        print ("category line 34"*10)
        if (len(f)==0):
            Category.objects.create(CategoryName=new_cat)
            catID=Category.objects.latest('id')
        else:
            print("Cat Id"*100)
            print f
            catID=f[0]
    else:
        print("Categgory"*100)
        print(request.POST['Category'])
        category=Category.objects.filter(id=request.POST['Category'])[0]
        catID=category

    # Grabbing list of ingredients
    mixes={}
    List_of_quantity=[]
    List_of_ingredients=[]
    for key in request.POST:
        if (re.match(r'[igr]',key)):
            # print(request.POST)
            num=re.search(r'\d+',key).group()
            mixes[num]=[request.POST[key]]
            # List_of_ingredients.append(request.POST[key])
    for qty in request.POST:
        if (re.match(r'[qty]',qty)):
                # print(request.POST)
                # print (qty)
                num= re.search(r'\d+',qty).group()
                mixes[num].append(request.POST[qty])

    print("mixes"*10)
    print(mixes)

    # *****check
    # mixes[i][0]=="Ingredient"
    # mixes[i][1]=="quantity"

    # Seperating inputs for RecipeManager
    I_data={
        "DishName": request.POST['DishName'],
        "Procedure": request.POST['Procedure'],
        "CookTime":  request.POST['CookTime'],
        "YoutubeLink":  request.POST['YoutubeLink'],
    }

    # image upload
    foodImage = request.FILES['foodimg']
    description=request.POST['Description']
    # fs = FileSystemStorage()
    # filename = fs.save(myfile.name, myfile)
    # uploaded_file_url = fs.url(filename)
    # print ("uploaded file url "*50)
    # print (uploaded_file_url)

    # Creating new Recipe and grabbing recipe Id
    Recipe_id=None
    results=Recipes.objects.check_recipe(I_data)
    if (results['status']):
        print("Category Id line 84"*10,catID)
        Recipes.objects.create(DishName=I_data['DishName'],Procedure=I_data['Procedure'],CookTime=I_data['CookTime'],YoutubeLink=I_data['YoutubeLink'],CategoryId=catID,Image=foodImage, Description=description)
        Recipe_id=Recipes.objects.latest('id')
        for n in mixes:
            Mix.objects.create(Quantity=mixes[n][1],IngredientName=mixes[n][0],RecipeId=Recipe_id)

        return redirect(reverse('recipe:show_path'))

    else:
        context={
            'errors': results['errors'],
            'categories': Category.objects.all(),
        }
        return render(request, 'recipeadmin/newrecipe.html', context)

    return redirect(reverse ('recipe:index_path'))


def logout(request):
    # session_keys = list(request.session.keys())
    # for k in request.session.keys():
    #     request.session.modified=True
    #     request.session.pop(k,None)
    request.session.clear()

    return redirect('recipeadmin:index_path')

