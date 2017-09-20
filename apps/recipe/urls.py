from django.conf.urls import url
from . import views
app_name="recipe"
urlpatterns = [
    url(r'^$', views.index, name = 'index_path'),
    url(r'^recipes$', views.show, name = 'show_path'),
    # url(r'^logout$', views.logout, name = 'logout_path')
  ]
