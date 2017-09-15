# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#class RecipeManager(models.Manager):
    

# Create your models here.
class Recipes(models.Model):
    DishName = models.CharField(max_length=255)
    CookTime = models.CharField(max_length=78)
    PrepTime = models.CharField(max_length=78)
    YoutubeLink = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    #objects = RecipeManager()

class Ingredients(models.Model):
    Name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    #objects = RecipeManager()

class Category(models.Model):
    CategoryName = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    #objects = RecipeManager()

class Mix(models.Model):
    Quantity = models.CharField(max_length=255)
    Procedure = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    IngredientId = models.ForeignKey(Ingredients, related_name="createdingred")
    RecipeId = models.ForeignKey(Recipes, related_name="createdrecipes")
    #objects = RecipeManager()


