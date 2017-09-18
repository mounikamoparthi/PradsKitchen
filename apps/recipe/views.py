# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from ..recipe.models import Recipes, Mix, Category


# Create your views here.
def index(request):
    # context={
    #     'recipes': Recipes.objects.all()
    # }
    return render(request, 'recipe/index.html');

def show(request):
    context={
        'recipes': Recipes.objects.all(),
        'mixes': Mix.objects.all(),
        'f': "x",
        "s": "x"
    }
    return render(request, 'recipe/show.html', context);
