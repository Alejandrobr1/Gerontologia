from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import TUsuario, TLogin
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, "index.html")

def loginup(request):
    if request.method == 'GET':
        return render(request,'login.html',{
        'form':AuthenticationForm
        })        
    else:
        user = authenticate(username=request.POST['correo'], password=request.POST['contrasena'])

        if user is None:
            return render(request,'login.html', {
            'form':AuthenticationForm,
            'error': 'El usuario o contrasena son incorrectos'
            })    
        else: 
            login(request, user)
            return redirect('especialidades')
        
    

def especialidades(request):
    return render(request, "especialidades.html")



def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form': UserCreationForm()
        })
    else:
        # Obtener datos del formulario
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        confirmar_contrasena = request.POST.get('confirmar_contrasena')
        nombres = request.POST.get('nombres')
        primer_apellido = request.POST.get('primer_apellido')
        segundo_apellido = request.POST.get('segundo_apellido')
        documentoid = request.POST.get('documentoid')
        celular = request.POST.get('celular')
        ciudad = request.POST.get('ciudad')
        direccion = request.POST.get('direccion')
        

        # Validar que las contraseñas coincidan
        if contrasena != confirmar_contrasena:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'registro.html', {
                'form': UserCreationForm()
            })

        # Validar que el correo no esté registrado
        if User.objects.filter(username=correo).exists() or TUsuario.objects.filter(correo=correo).exists():
            messages.error(request, 'El correo electrónico ya está registrado.')
            return render(request, 'registro.html', {
                'form': UserCreationForm()
            })

        try:
            # Crear el usuario en la tabla User de Django
            user = User.objects.create_user(
                username=correo,  # Usar el correo como nombre de usuario
                password=contrasena
            )
            user.save()

            # Crear el registro en la tabla TUsuario
            tuser = TUsuario(
                nombre=nombres,
                primer_apellido=primer_apellido,
                segundo_apellido=segundo_apellido,
                documento=documentoid,
                celular=celular,
                correo=correo,
                ciudad=ciudad,
                direccion=direccion,
                rol=0
            )
            tuser.save()

            tlogin = TLogin(
                contrasena=contrasena
            )
            tuser.save()

            # Iniciar sesión automáticamente
            login(request, user)
            messages.success(request, 'Registro exitoso. Bienvenido.')
            return redirect('especialidades')

        except Exception as e:
            # Manejar errores específicos
            messages.error(request, f'Error al registrar el usuario: {str(e)}')
            return render(request, 'registro.html', {
                'form': UserCreationForm()
            })
  

def cerrarSesion(request):
    logout(request)
    return redirect('home')
  