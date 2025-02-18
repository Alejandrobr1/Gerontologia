from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
#from django.contrib.auth import login
# Create your views here.
def home(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def registro3(request):
    return render(request, "registro3.html")


def registro(request):
  if request.method == 'GET':
        return render(request,'registro.html',{
        'form':UserCreationForm
        })
        print("Enviando formulario")
  else:
     if request.POST['contrasena'] == request.POST['confirmar_contrasena']:
        try: 
           user=User.objects.create_user(username=request.POST['correo'], password=request.POST['contrasena'])
           user.save()
           login(request, user)
           return HttpResponse('enviar formulario')
        except:
           return HttpResponse('usuario ya existente')
  return HttpResponse('contraseñas no coinciden')
        
  

"""def registro(request):
   
   if request.method == 'GET':
     return render(request, "registro.html", {
      'form': UserCreationForm 
      })
      #print("Enviando formulario")
   else:
      if request.POST['password1']==request.POST['password2']:
         #registe user
         try:
            user=User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            user.save
            login(request, user)
            return redirect('index')
         except:
            return render(request, "registro.html", {
            'form': UserCreationForm,
            'error': 'El usuario ya existe'
            })
      return render(request, "registro.html", {
            'form': UserCreationForm,
            'error': 'la contrasena no coincide'
            })
      #print(request.POST)
      #print("obteniendo datos")  """

#def index(request):
   #return render(request, "index.html")
  