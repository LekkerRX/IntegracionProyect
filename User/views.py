from django.shortcuts import render
from django.shortcuts import render, redirect

from django.contrib import messages
from django.shortcuts import redirect

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login


def pagina_inicio(request):
    # apararecer solo when is_home is false
    is_homepage = True
    return render(request, 'Homepagefromhomepage.html', {'is_homepage': is_homepage})





from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TecnicoForm,EditProfileForm
from .models import Tecnico





from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login



from django.contrib.auth import get_user_model

# views.py
from django.shortcuts import render

def pagina_tecnico(request):
    return render(request, 'HomepageTecnic.html')


def pagina_cliente(request):
    return render(request, 'HomepageClient.html')

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import EmailAuthenticationForm

from django.contrib.auth import authenticate, login

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('User:perfil_tecnico')

    form = EmailAuthenticationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # Especificamos el backend para la autenticación de los técnicos
            user = authenticate(request=request, email=form.cleaned_data['email'], password=form.cleaned_data['password'], backend='User.authentication_backend.CustomBackend')
            
            if user is not None:
                login(request, user, backend='User.authentication_backend.CustomBackend')
                return redirect('User:perfil_tecnico')
            else:
                form.add_error(None, "Correo o contraseña inválidos.")

    return render(request, 'HomepageTecnic.html', {'form': form})


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import ClientLoginForm


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import ClientLoginForm  # Asegúrate de tener el formulario de cliente adecuado

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import ClientLoginForm

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ClientLoginForm

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import ClientLoginForm

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import ClientLoginForm

def client_login_client(request):
    if request.user.is_authenticated:
        return redirect('Post:gestionar_publicaciones')

    form = ClientLoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        if user:
            login(request, user)
            return redirect('Post:gestionar_publicaciones')

    return render(request, 'HomepageClient.html', {'form': form})








from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tecnico  # Asegúrate de importar tu modelo
from .forms import ImagenPerfilForm  # Formulario para subir imagen (si es necesario)
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ImagenPerfilForm
from .models import Tecnico
from django.contrib.auth import logout


def custom_logout(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('User:pagina_inicio')  # Redirige a la página de inicio de sesión






def perfil_tecnico(request):
    tecnico = get_object_or_404(Tecnico, user=request.user)
    user = User.objects.get(id=tecnico.user.id)
    
     # Suponiendo que tienes una forma de obtener los días y horas de trabajo
    dias_trabajo = tecnico.horario_disponible.split(' desde ')[0].split(', ') if tecnico.horario_disponible else []
    hora_inicio = tecnico.horario_disponible.split('desde las ')[1].split(' hasta ')[0] if 'desde' in tecnico.horario_disponible else ''
    hora_fin = tecnico.horario_disponible.split('hasta las ')[1] if 'hasta' in tecnico.horario_disponible else ''
    
    

    # Limpiar la cadena para obtener solo los nombres de las comunas
    if tecnico.localidades:
        localidades_str = tecnico.localidades
        cleaned_str = localidades_str.replace("<QuerySet [", "").replace("]>", "")
        localidades_nombres = [loc.strip().split(': ')[1].replace('>', '') for loc in cleaned_str.split(', ') if loc.strip()]
    else:
        localidades_nombres = []

    # Procesar el horario para enviarlo al template
    horarios = []
    horas = None

    if tecnico.horario_disponible:
        partes = tecnico.horario_disponible.split(' desde ')
        dias = partes[0].split(', ')
        if len(partes) > 1:
            horas = partes[1].strip()
        for dia in dias:
            horarios.append({'dia': dia.strip(), 'horas': horas})

    if request.method == 'POST':
        form = ImagenPerfilForm(request.POST, request.FILES, instance=tecnico)
        if form.is_valid():
            # Actualiza el técnico
            
            form.save()

            # Actualiza el correo en auth_user
            user.email = form.cleaned_data['correo']
            user.save()

            messages.success(request, 'Perfil actualizado exitosamente.')
            return redirect('User:perfil_tecnico')  # Redirige a la página de perfil u otra
        else:
            messages.error(request, 'Hubo un error al actualizar el perfil. Inténtalo de nuevo.')
    else:
        form = ImagenPerfilForm(initial={
            'correo': user.email,  # Cargar el correo desde auth_user
            'nombre': tecnico.nombre,
            'horario_disponible': tecnico.horario_disponible,
            'dias_trabajo': dias_trabajo,
            'hora_inicio': hora_inicio,
            'hora_fin': hora_fin,
          
        })
        

    context = {
        'tecnico': tecnico,
        'email': request.user.email,
        'form': form,
        'localidades': localidades_nombres,
        'horarios': horarios,
        'nombre_tecnico': tecnico.nombre.title() if tecnico.nombre else '',  # Mayúsculas independiente de BD
    }
    
    return render(request, 'perfilTecnico.html', context)



from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import TecnicoForm

from django.contrib import messages

def registro_tecnico(request):
    if request.method == 'POST':
        form = TecnicoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Crear el usuario
                user = User(
                    username=form.cleaned_data['nombre'],
                    email=form.cleaned_data['email']
                )
                user.set_password(form.cleaned_data['password1'])
                user.save()
                
                # Crear el perfil de Técnico
                tecnico = form.save(commit=False)
                tecnico.user = user
                
                # Guardar días y horas disponibles
                dias_seleccionados = ', '.join(form.cleaned_data['dias_trabajo'])
                tecnico.horario_disponible = f"{dias_seleccionados} desde las {form.cleaned_data['hora_inicio']} hasta las {form.cleaned_data['hora_fin']}"
                tecnico.save()
                
                return redirect('User:pagina_inicio')
            except Exception as e:
                messages.error(request, f"Error al registrar: {e}")
    else:
        form = TecnicoForm()

    return render(request, 'register.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ClientRegistrationForm

# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import ClientRegistrationForm

from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import ClientRegistrationForm


from django.contrib.auth import login
from django.contrib.auth.backends import ModelBackend  # Importa el backend que prefieras

def client_register(request):
    if request.user.is_authenticated:
        return redirect('User:pagina_cliente')  # Redirigir si ya está autenticado

    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            try:
                # Crear el usuario
                user = User(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email']
                )
                user.set_password(form.cleaned_data['password1'])
                user.save()

                # Autenticar y redirigir, especificando el backend
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, "¡Registro exitoso!")
                return redirect('User:pagina_cliente')  # Redirigir a la página de inicio o perfil
            except Exception as e:
                messages.error(request, f"Error al registrar el cliente: {e}")
    else:
        form = ClientRegistrationForm()

    return render(request, 'register_client.html', {'form': form})



