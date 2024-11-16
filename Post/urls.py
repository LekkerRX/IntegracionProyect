from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Post' 

urlpatterns = [
    
    path('gestionar_publicaciones/', views.gestionar_publicaciones, name='gestionar_publicaciones'),
    path('eliminar_publicacion/<int:publicacion_id>/', views.eliminar_publicacion, name='eliminar_publicacion'),
    



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)