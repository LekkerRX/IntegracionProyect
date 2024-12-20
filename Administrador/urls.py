# urls.py
from django.urls import path
from . import views

app_name = 'Administrador' 

urlpatterns = [
    path('admin/credenciales/', views.lista_credenciales, name='lista_credenciales'),
    path('admin/credenciales/verificar/<int:credencial_id>/', views.verificar_credencial, name='verificar_credencial'),
    path('admin/credenciales/rechazar/<int:credencial_id>/', views.rechazar_credencial, name='rechazar_credencial'),
    path('admin/gestionar_publicaciones/', views.gestionar_publicaciones, name='gestionar_publicaciones'),
    path('notificacion/<int:notificacion_id>/marcar_como_leida/', views.marcar_como_leida_admin, name='marcar_como_leida_admin'),
    path('notificacion/<int:notificacion_id>/marcar_como_leida/', views.marcar_como_leida_tecnico, name='marcar_como_leida_tecnico'),
    path('notificacion/<int:notificacion_id>/marcar_como_leida/', views.marcar_como_leida_usuario, name='marcar_como_leida_usuario'),
    
]

