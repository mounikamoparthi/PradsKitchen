# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class RecipeManager(models.Manager):

    def check_recipe(self,postData):
        results={'status': True, 'errors':[], 'recipe':None}
        if not postData['DishName'] or len(postData['DishName'])<3:
            print "DishName Error"
            results['status'] = False
            results['errors'].append("Please enter valid DishName")

        if not postData['CookTime'] or postData['CookTime']< 0 :
            print "CookTime Error"
            results['status'] = False
            results['errors'].append("Please enter valid CookTime")

        if not postData['Procedure'] or len(postData['Procedure'])< 10 :
            print "YoutubeLink Error"
            results['status'] = False
            results['errors'].append("Procedure needs to be more than 10characters in length")

        if not postData['YoutubeLink'] or len(postData['YoutubeLink'])< 3 :
            print "YoutubeLink Error"
            results['status'] = False
            results['errors'].append("Please enter valid Youtube Link")

        return results



class IngredientManager(models.Manager):

    def check_ingredient(self,postData):
        results={'status': True, 'errors':[], 'ingredient':None}
        if not postData['Name'] or len(postData['Name'])<3:
            print "Ingredient Error"
            results['status'] = False
            results['errors'].append("Please enter valid Ingredient")

class CategoryManager(models.Manager):

    def check_category(self,postData):
        results={'status': True, 'errors':[], 'category':None}
        print (postData)
        # if not postData['CategoryName'] or len(postData['CategoryName']<3):
        #     print "CategoryName Error"
        #     results['status'] = False
        #     results['errors'].append("Please enter valid CategoryName")

class MixManager(models.Manager):

    def check_Quantity(self,postData):
        results={'status': True, 'errors':[], 'mix':None}
        if not postData['Quantity']:
            print "Quantity Error"
            results['status'] = False
            results['errors'].append("Please enter valid Quantity")




# Create your models here.
class Recipes(models.Model):
    DishName = models.CharField(max_length=255)
    CookTime = models.CharField(max_length=78)
    Procedure = models.TextField()
    YoutubeLink = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = RecipeManager()

class Ingredients(models.Model):
    Name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = IngredientManager()

class Category(models.Model):
    CategoryName = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CategoryManager()

class Mix(models.Model):
    Quantity = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    IngredientId = models.ForeignKey(Ingredients, related_name="createdingred")
    RecipeId = models.ForeignKey(Recipes, related_name="createdrecipes")
    objects = MixManager()
