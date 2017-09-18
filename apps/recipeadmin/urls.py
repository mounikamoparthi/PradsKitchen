from django.conf.urls import url
from .import views 
app_name = 'recipeadmin'
urlpatterns = [
    url(r'^$', views.index, name = "index_path"),
    url(r'^login$', views.login, name = "login_path"),
    url(r'^register$', views.registration, name = "reg_path"),
    url(r'^new$', views.new, name = "new_path"),
    url(r'^create$', views.create, name = "create_path")
]