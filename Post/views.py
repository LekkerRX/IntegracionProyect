from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PublicacionForm
from .models import Publicacion

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Publicacion

@login_required
def eliminar_publicacion(request, publicacion_id):
    # Intentamos obtener la publicación, si no existe se lanza un 404
    publicacion = get_object_or_404(Publicacion, id=publicacion_id, cliente=request.user)
    
    # Eliminar la publicación
    publicacion.delete()
    
    # Mensaje de éxito
    messages.success(request, 'La publicación ha sido eliminada correctamente.')
    
    # Redirigir de nuevo a la página de gestionar publicaciones
    return redirect('Post:gestionar_publicaciones')


@login_required
def gestionar_publicaciones(request):
    # Obtener el parámetro de orden de la URL (si existe)
    sort_order = request.GET.get('sort', 'desc')  # Por defecto, ordenar de mayor a menor

    # Filtrar las publicaciones del usuario
    publicaciones = Publicacion.objects.filter(cliente=request.user)

    # Ordenar las publicaciones según el parámetro 'sort'
    if sort_order == 'asc':
        publicaciones = publicaciones.order_by('fecha_publicacion')  # Ascendente
    else:
        publicaciones = publicaciones.order_by('-fecha_publicacion')  # Descendente

    # Si el formulario se envía, procesamos la creación o edición
    if request.method == 'POST':
        # Verificamos si es una publicación existente o una nueva
        publicacion_id = request.POST.get('publicacion_id')  # Obtener el ID de la publicación si está presente

        # Si existe el ID, buscamos la publicación para editarla, si no es un nuevo formulario
        if publicacion_id:
            try:
                publicacion = Publicacion.objects.get(id=publicacion_id, cliente=request.user)
                form = PublicacionForm(request.POST, request.FILES, instance=publicacion, user=request.user)
            except Publicacion.DoesNotExist:
                form = PublicacionForm(request.POST, request.FILES, user=request.user)
        else:
            # Si no hay ID, significa que es una nueva publicación
            form = PublicacionForm(request.POST, request.FILES, user=request.user)

        if form.is_valid():
            form.save()  # Guarda o actualiza la publicación
            messages.success(request, 'Publicación guardada correctamente.')  # Mensaje de éxito
            return redirect('Post:gestionar_publicaciones')
        else:
            messages.error(request, 'Hubo un error al guardar la publicación. Inténtalo de nuevo.')  # Mensaje de error

    else:
        # En la vista GET, si se pasa un ID, se edita la publicación
        publicacion_id = request.GET.get('publicacion_id')
        if publicacion_id:
            try:
                publicacion = Publicacion.objects.get(id=publicacion_id, cliente=request.user)
                form = PublicacionForm(instance=publicacion, user=request.user)
            except Publicacion.DoesNotExist:
                form = PublicacionForm(user=request.user)
        else:
            form = PublicacionForm(user=request.user)

    return render(request, 'gestionar_publicaciones.html', {'form': form, 'publicaciones': publicaciones})
