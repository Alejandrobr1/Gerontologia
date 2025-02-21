from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import TUsuario, TLogin
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

#este metodo retorna a la vista principal
def home(request):
    return render(request, "index.html")

#este metodo retorna a la vista quienes somos
def somos(request):
    return render(request, "quienes-Somos.html")

#este método inicia la sesion del usuario
def loginup(request):
    if request.method == 'GET': #si se hace la petición al servidor entonces este devuelve la vista de login
        return render(request,'login.html',{
        'form':AuthenticationForm #AuthenticationForm se encarga de enviar un formulario al contexto de la plantilla
        })        
    else:
        user = authenticate(username=request.POST['correo'], 
                            password=request.POST['contrasena']) # almacena el usuario en una variable user y autentifica el usuario y contraseña enviados

        if user is None: #si el usuario y/o contraseña no existen entonces muestra nuevamente la vista login
            return render(request,'login.html', { 
            'form':AuthenticationForm,
            'error': 'El usuario o contraseña son incorrectos' #si no coincide el usuario y contraseña, imprime el error y renderiza la vista de login nuevamente
            })    
        else: #si el usuario existe en la base de datos y ademas coincide la contraseña, se redirige al usuario a la pagina de inicio
            login(request, user)
            return redirect('home')
        
    
#este metodo retorna a la vista especialidades
def especialidades(request):
    return render(request, "especialidades.html")


#este metodo retorna registra al usuario
def registro(request):
    if request.method == 'GET':#si se hace la petición al servidor entonces este devuelve la vista de registro
        return render(request, 'registro.html', { 
            'form': UserCreationForm()#UserCrfeationForm se encarga de crear un formulario en el contexto de la plantilla
        })
    else:
        #A continuación se almacenan lo datos escritos por el usuario en el formulario en variables
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
        

        #Se valida que las contraseñas coincidan
        if contrasena != confirmar_contrasena:
            messages.error(request, 'Las contraseñas no coinciden.') #Se mostrará un mensaje al usuario que indica que las contraseñas creadas no coinciden
            return render(request, 'registro.html', { #Se renderiza nuevamente la vista de registro y se crea un nuevo formulario
                'form': UserCreationForm()
            })

        #Se valida que el correo no esté registrado
        if User.objects.filter(username=correo).exists() or TUsuario.objects.filter(correo=correo).exists(): #Se busca el correo en las tablas de la clase User y TUsuario y si este existe devuelve un error
            messages.error(request, 'El correo electrónico ya está registrado.') # se imprimirá el error indicando que el usuario o correo electronico ya esta registrado
            return render(request, 'registro.html', { #Se renderiza nuevamente la vista de registro y se crea un nuevo formulario
                'form': UserCreationForm()
            })

        try:
            #Crea el usuario en la tabla User de Django
            user = User.objects.create_user(
                username=correo,  #Se crea el usuario a partir del correo
                password=contrasena #Se crea la contraseña del usuario 
            )
            user.save() #Se guarda el usuario en la tabla 

            #Crea el registro en la tabla TUsuario
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
            tuser.save() #Se guarda el usuario en la tabla

            tlogin = TLogin(
                contrasena=contrasena #Se guarda la contraseña en la tabla de TLogin
            )
            tuser.save() #Se guarda la contraseña en la tabla

            #Iniciar sesión automáticamente
            login(request, user)
            messages.success(request, 'Registro exitoso. Bienvenido.') #se le envia un mensaje al usuario de que el registro fue exitoso
            return redirect('home') #se redirecciona a la pagina de home

        except Exception as e:
             
            messages.error(request, f'Error al registrar el usuario: {str(e)}')#Se muestra especificamente el error ocurrido al intentar guardar el usuario y no lograrlo exitosamente
            return render(request, 'registro.html', {
                'form': UserCreationForm() #UserCrfeationForm se encarga de crear un formulario en el contexto de la plantilla
            })
  
#este metodo cierra la sesion del usuario y redirecciona al usuario a la pagina principal 
def cerrarSesion(request):
    logout(request)
    return redirect('home')
  