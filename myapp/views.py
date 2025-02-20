from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
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
        
    

def registro3(request):
    return render(request, "registro3.html")

def especialidades(request):
    return render(request, "especialidades.html")


    



def registro(request):
  if request.method == 'GET':
        return render(request,'registro.html',{
        'form':UserCreationForm
        })
        
  else:
     if request.POST['contrasena'] == request.POST['confirmar_contrasena']:
        try: 
           user=User.objects.create_user(username=request.POST['correo'], password=request.POST['contrasena'])
           user.save()
           login(request, user)
           return redirect('especialidades')
           
           
        except:
           return render(request, 'registro.html', {
               'form':UserCreationForm,
               "error": 'ya existre el usuario'
           })
  return HttpResponse('contraseñas no coinciden')
        
  

def cerrarSesion(request):
    logout(request)
    return redirect('home')
  