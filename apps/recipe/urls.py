from django.conf.urls import url
from . import views
app_name="recipe"          
urlpatterns = [
    url(r'^$', views.index, name = 'index_path'),
  ]