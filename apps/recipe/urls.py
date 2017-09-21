from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name="recipe"
urlpatterns = [
    url(r'^$', views.index, name = 'index_path'),
    url(r'^recipes$', views.show, name = 'show_path'),
    # url(r'^logout$', views.logout, name = 'logout_path')
  ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  
  # if settings.DEBUG:
  #   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
