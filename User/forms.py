


import re 
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django import forms

from django import forms
from .models import Tecnico

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Tecnico,Localidad

COMUNAS_SANTIAGO = [
    ('Cerrillos', 'Cerrillos'),
    ('Cerro Navia', 'Cerro Navia'),
    ('Conchalí', 'Conchalí'),
    ('El Bosque', 'El Bosque'),
    ('Estación Central', 'Estación Central'),
    ('Huechuraba', 'Huechuraba'),
    ('Independencia', 'Independencia'),
    ('La Cisterna', 'La Cisterna'),
    ('La Florida', 'La Florida'),
    ('La Granja', 'La Granja'),
    ('La Pintana', 'La Pintana'),
    ('La Reina', 'La Reina'),
    ('Las Condes', 'Las Condes'),
    ('Lo Barnechea', 'Lo Barnechea'),
    ('Lo Espejo', 'Lo Espejo'),
    ('Lo Prado', 'Lo Prado'),
    ('Macul', 'Macul'),
    ('Maipú', 'Maipú'),
    ('Ñuñoa', 'Ñuñoa'),
    ('Pedro Aguirre Cerda', 'Pedro Aguirre Cerda'),
    ('Peñalolén', 'Peñalolén'),
    ('Providencia', 'Providencia'),
    ('Pudahuel', 'Pudahuel'),
    ('Quilicura', 'Quilicura'),
    ('Quinta Normal', 'Quinta Normal'),
    ('Recoleta', 'Recoleta'),
    ('Renca', 'Renca'),
    ('San Joaquín', 'San Joaquín'),
    ('San Miguel', 'San Miguel'),
    ('San Ramón', 'San Ramón'),
    ('Santiago', 'Santiago'),
    ('Vitacura', 'Vitacura'),
]





from django import forms


from .models import Tecnico  # Asegúrate de importar el modelo correspondiente

from django import forms
from django.contrib.auth.models import User
from .models import Tecnico

# En forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Tecnico

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Tecnico  # Asegúrate de importar tu modelo Tecnico

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User



class ImagenPerfilForm(forms.ModelForm):
    DIAS = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ]
    localidades = forms.ModelMultipleChoiceField(
        queryset=Localidad.objects.all(),  # Obtén todas las localidades de la base de datos
        widget=forms.CheckboxSelectMultiple,  # Puedes usar Checkboxes para selección múltiple
        label="Localidades Disponibles",
        error_messages={'required': 'Este campo es obligatorio.'}
    )
    
    dias_trabajo = forms.MultipleChoiceField(
        choices=DIAS,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-inline'}),  # Clases de Bootstrap
        label="Días de Trabajo",
        required=False
    )



    

    hora_inicio = forms.ChoiceField(
        choices=[(f"{h}:00", f"{h}:00") for h in range(24)],
        label="Hora de Inicio",
        widget=forms.Select(attrs={'class': 'form-select'})  # Clase Bootstrap para select
    )

    hora_fin = forms.ChoiceField(
        choices=[(f"{h}:00", f"{h}:00") for h in range(24)],
        label="Hora de Fin",
        widget=forms.Select(attrs={'class': 'form-select'})  # Clase Bootstrap para select
    )

    correo = forms.EmailField(
        required=True,
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
        error_messages={
            'required': 'Este campo es obligatorio.',
            'invalid': 'Ingrese una dirección de correo electrónico válida.',
        }
    )

    class Meta:
        model = Tecnico
        fields = ['imagen_perfil', 'nombre', 'correo', 'dias_trabajo', 'hora_inicio', 'hora_fin','localidades']
        widgets = {
            'imagen_perfil': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(ImagenPerfilForm, self).__init__(*args, **kwargs)
        self.fields['dias_trabajo'].initial = kwargs.get('initial', {}).get('dias_trabajo', [])
        
        self.fields['hora_inicio'].initial = kwargs.get('initial', {}).get('hora_inicio', '')
        self.fields['hora_fin'].initial = kwargs.get('initial', {}).get('hora_fin', '')
        if 'instance' in kwargs:
            self.old_email = kwargs['instance'].user.email
        else:
            self.old_email = None  # Si no hay instancia, no hay correo anterior.

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        # Solo verifica si el correo ha cambiado
        if correo and correo != self.old_email and User.objects.filter(email=correo).exists():
            raise ValidationError('Este correo electrónico ya está registrado.')
        return correo

    def save(self, commit=True):
        tecnico = super().save(commit=False)
        
        # Construir la cadena de horario disponible
        dias_seleccionados = ', '.join(self.cleaned_data['dias_trabajo'])
        horario = f"{dias_seleccionados} desde las {self.cleaned_data['hora_inicio']} hasta las {self.cleaned_data['hora_fin']}"
        tecnico.horario_disponible = horario
        
        if commit:
            tecnico.save()
        
        return tecnico

    
    




# forms.py
from django import forms
from .models import Tecnico

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = ['nombre', 'ubicacion','horario_disponible', 'especialidades', 'credenciales', 'imagen_perfil']


class TecnicoForm(forms.ModelForm):
    DIAS = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ]

    dias_trabajo = forms.MultipleChoiceField(
        choices=DIAS,
        widget=forms.CheckboxSelectMultiple,
        label="Días de Trabajo",
    )

    hora_inicio = forms.ChoiceField(
        choices=[(f"{h}:00", f"{h}:00") for h in range(24)],
  # Añadir clase Bootstrap y tipo time        label="Hora de Inicio",
    )

    hora_fin = forms.ChoiceField(
        choices=[(f"{h}:00", f"{h}:00") for h in range(24)],
        label="Hora de Fin",
   
    )
    nombre = forms.CharField(
        label="Nombre",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
        error_messages={'required': 'Este campo es obligatorio.'}
    )
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
        error_messages={
            'required': 'Este campo es obligatorio.',
            'invalid': 'Ingrese una dirección de correo electrónico válida.',
        }
    )
    
    
    horario_disponible = forms.CharField(
        label="Horario Disponible",
        required=False,
        widget=forms.HiddenInput()
    )
    
    ubicacion = forms.ChoiceField(
        label="Ubicación",
        choices=COMUNAS_SANTIAGO,  # Usar la lista de comunas
        widget=forms.Select(attrs={'class': 'form-control'}),
        error_messages={'required': 'Este campo es obligatorio.'}
    )
    
    ubicacion = forms.ChoiceField(
        label="Ubicación",
        choices=COMUNAS_SANTIAGO,  # Usar la lista de comunas
        widget=forms.Select(attrs={'class': 'form-control'}),
        error_messages={'required': 'Este campo es obligatorio.'}
    )
    
    localidades = forms.ModelMultipleChoiceField(
        queryset=Localidad.objects.all(),  # Obtén todas las localidades de la base de datos
        widget=forms.CheckboxSelectMultiple,  # Puedes usar Checkboxes para selección múltiple
        label="Localidades Disponibles",
        error_messages={'required': 'Este campo es obligatorio.'}
    )

    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        error_messages={'required': 'Este campo es obligatorio.'}
    )

    password2 = forms.CharField(
        label="Confirmar Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'}),
        error_messages={'required': 'Este campo es obligatorio.'}
    )
    
    

    class Meta:
        model = Tecnico
        fields = ['nombre', 'ubicacion', 'horario_disponible', 'especialidades', 'credenciales', 'localidades', 'email', 'password1', 'password2']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'horario_disponible': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Horario disponible'}),
            'especialidades': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Especialidades, separadas por comas'}),
            'localidades': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Localidades en las que trabaja'}),
            'credenciales': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está registrado.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden. Por favor, ingrese las mismas contraseñas en ambos campos.")

        # Aquí podrías agregar más validaciones para la contraseña si lo deseas

from django import forms
from django.contrib.auth import authenticate


# forms.py
from django import forms
from django.contrib.auth import authenticate





class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254,
                              widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
                              error_messages={
                                  'required': 'Este campo es obligatorio.',
                                  'invalid': 'Ingrese una dirección de correo electrónico válida.',
                              }
                              )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        error_messages={'required': 'Este campo es obligatorio.'}
    )

    def clean(self):
        cleaned_data = super().clean()  # Llama al método clean del padre
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user is None:
                raise forms.ValidationError("Correo o contraseña inválidos.")

        return cleaned_data

    def get_user(self):
        return self.user if hasattr(self, 'user') else None


# forms.py
from django import forms
from django.contrib.auth import authenticate

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class ClientLoginForm(forms.Form):
    email = forms.EmailField(
        label="Correo Electrónico", max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
        error_messages={
            'required': 'Este campo es obligatorio.',
            'invalid': 'Ingrese una dirección de correo electrónico válida.',
        }
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        error_messages={'required': 'Este campo es obligatorio.'}
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            # Usar el backend de autenticación específico para correo
            user = authenticate(email=email, password=password, backend='User.authentication_backend.EmailBackend')

            if user is None:
                # Verifica si el error es por correo o contraseña
                try:
                    user_check = User.objects.get(email=email)
                except User.DoesNotExist:
                    raise forms.ValidationError("El correo electrónico no está registrado.")
                
                raise forms.ValidationError("La contraseña es incorrecta.")
            
            self.user = user

        return cleaned_data

    def get_user(self):
        return getattr(self, 'user', None)



# forms.py
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

# forms.py
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import re

# Validador personalizado para el nombre de usuario
def username_validator(value):
    pattern = re.compile(r'^[a-zA-Z0-9]*$')
    if not pattern.match(value):
        raise ValidationError('Ingrese un nombre de usuario válido (solo letras y números).')

class ClientRegistrationForm(forms.Form):
    username = forms.CharField(
        label="Nombre de usuario único",
        strip=False,
        help_text="",
        validators=[username_validator],  # Usar la función de validador personalizada
        error_messages={
            'required': 'Este campo es obligatorio.',
            'invalid': 'Ingrese un nombre de usuario válido.',
        }
    )

    email = forms.EmailField(
        max_length=254,
        validators=[
            RegexValidator(
                regex=r'^\S+@\S+\.\S+$',
                message="Ingrese una dirección de correo electrónico válida.",
                code='invalid_email'
            )
        ],
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'})
    )

    password1 = forms.CharField(
        label="Contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text="La contraseña debe tener al menos 8 caracteres y contener al menos una mayúscula, un número y un carácter especial (@, #, $, %, ^, &, +, =, !).",
        error_messages={
            'required': 'Este campo es obligatorio.',
        }
    )

    password2 = forms.CharField(
        label="Confirmar Contraseña",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        error_messages={
            'required': 'Este campo es obligatorio.',
        }
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya está registrado.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está registrado.")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if not re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$', password1):
            raise ValidationError(
                "La contraseña debe tener al menos 8 caracteres y contener al menos una mayúscula, un número y un carácter especial (@, #, $, %, ^, &, +, =, !)."
            )
        return password1

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden.")
        
        return cleaned_data

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            password=self.cleaned_data["password1"],
        )
        return user
