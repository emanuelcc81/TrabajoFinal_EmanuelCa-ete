from django.http import HttpResponse
from django.shortcuts import render, redirect
from app_negocio.models import Avatar, Productos
from app_negocio.models import Datos_productos
from app_negocio.models import Proveedores
from django.template import loader
from app_negocio.forms import Productos_formulario, UserEditForm
from app_negocio.forms import Datos_formulario
from app_negocio.forms import Proveedores_formulario
import datetime
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.




def inicio(request):
   
    return render ( request, "padre.html")


@login_required
def productos(request):
    producto = Productos.objects.all()
        
    return render( request , "productos.html", {"producto": producto} )

@login_required
def productos_formulario(request):

    if request.method == "POST":

        mi_formulario = Productos_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            producto = Productos( nombre=datos['nombre'] , precio=datos['precio'])
            producto.save()
            
            producto = Productos.objects.all()
            
            return render( request , "productos.html", {"producto": producto} )

    return render( request, "formulario_productos.html")


def buscar_producto(request):

    return render( request , "buscar_productos.html")


def resultado_productos(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        producto = Productos.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_productos.html" , {"productos": producto})
    else:
        return HttpResponse("Campo vacio")

@login_required
def elimina_producto( request, id):
   
    producto=Productos.objects.get(id=id)
    producto.delete()

    producto=Productos.objects.all()
    return render (request , "productos.html" , {"producto": producto})

@login_required
def modificar_producto(request, id):
    producto=Productos.objects.get(id=id)
    
    if request.method == "POST":

        mi_formulario = Productos_formulario( request.POST )
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data 
            producto.nombre = datos['nombre']  
            producto.precio = datos['precio']
            producto.save()

            producto = Productos.objects.all()
            return render( request , "productos.html", {"producto": producto} )   
        
    else:
        mi_formulario = Productos_formulario(initial={'nombre':producto.nombre , 'precio':producto.precio})
    
    return render (request , "modificar_productos.html" , {"mi_formulario":mi_formulario, "producto": producto})


@login_required    
def datos(request):
    datos = Datos_productos.objects.all()
        
    return render( request , "datos.html", {"datos": datos})


@login_required
def datos_formulario(request):

    if request.method == "POST":

        mi_formulario = Datos_formulario( request.POST )

        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data          
            
            datos = Datos_productos( nombre=info['nombre'] , marca=info['marca'], fecha_fab=info['fecha_fab'])
            datos.save()

            datos = Datos_productos.objects.all()
            
            return render( request , "datos.html", {"datos":datos} )

    return render( request, "formulario_datos.html")


@login_required
def elimina_datos( request, id):
    datos=Datos_productos.objects.get(id=id)
    datos.delete()

    datos=Datos_productos.objects.all()

    return render( request , "datos.html", {"datos":datos})


@login_required
def modificar_dato(request, id):
    datos=Datos_productos.objects.get(id=id)
    
    if request.method == "POST":

        mi_formulario = Datos_formulario( request.POST )
        
        if mi_formulario.is_valid():
            dato = mi_formulario.cleaned_data 
            datos.nombre = dato['nombre']  
            datos.marca = dato['marca']
            datos.fecha_fab = dato['fecha_fab']
            datos.save()

            datos=Datos_productos.objects.all()
            return render( request , "datos.html", {"datos":datos})   
        
    else:
        mi_formulario = Datos_formulario(initial={'nombre':datos.nombre , 'marca':datos.marca , 'fecha_fab':datos.fecha_fab} )
    
    return render (request , "modificar_datos.html" , {"mi_formulario":mi_formulario, "datos":datos})


@login_required    
def proveedores(request):
    proveedores = Proveedores.objects.all()
        
    return render( request , "proveedores.html", {"proveedores" : proveedores})


@login_required
def proveedores_formulario(request):

    if request.method == "POST":

        mi_formulario = Proveedores_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            proveedores = Proveedores( nombre=datos['nombre'] , telefono=datos['telefono'])
            proveedores.save()
            
            proveedores = Proveedores.objects.all()
            
            return render( request , "proveedores.html", {"proveedores":proveedores} )

    return render( request, "formulario_proveedores.html")


@login_required
def elimina_proveedores( request, id):
    proveedores=Proveedores.objects.get(id=id)
    proveedores.delete()

    proveedores=Proveedores.objects.all()

    return render( request , "proveedores.html", {"proveedores":proveedores})


@login_required
def modificar_proveedores(request, id):
    proveedores=Proveedores.objects.get(id=id)
    
    if request.method == "POST":

        mi_formulario = Proveedores_formulario( request.POST )
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data 
            proveedores.nombre = datos['nombre']  
            proveedores.precio = datos['telefono']
            proveedores.save()

            proveedores=Proveedores.objects.all()
            return render( request , "proveedores.html", {"proveedores":proveedores} )   
        
    else:
        mi_formulario = Proveedores_formulario(initial={'nombre':proveedores.nombre , 'telefono':proveedores.telefono})
    
    return render (request , "modificar_proveedores.html" , {"mi_formulario":mi_formulario, "proveedores":proveedores})


def login_request(request):
    if request.method =="POST":
        form= AuthenticationForm(request, data=request.POST)

        if form.is_valid():
           usuario = form.cleaned_data.get("username")
           clave_usuario= form.cleaned_data.get("password")

           user=authenticate(username=usuario , password=clave_usuario)
           
           if user is not None:
               login(request , user)
               avatares=Avatar.objects.filter(user=request.user.id)
               return render ( request , "inicio.html", {"url":avatares[0].image.url})
           else:
                return HttpResponse("Usuario incorrecto")
        else:
            return HttpResponse(f"Usuario incorrecto {form}")

    form = AuthenticationForm()

    return render( request, "login.html", {"form":form})


def registro(request):

    if request.method == "POST":
        form= UserCreationForm(request.POST)

        if form.is_valid():
           form.save()
           return HttpResponse("Usuario creado")

    else:
        form = UserCreationForm()
    return render(request , "registro.html" , {"form":form})    


@login_required
def editar_perfil(request):   
    usuario = request.user
    
    if request.method == "POST":
        mi_formulario = UserEditForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            usuario.email = informacion ['email']
            password = informacion['password1']
            
            usuario.set_password(password)
            usuario.save()

            return render(request , "inicio.html")     
    
    else:
        mi_formulario = UserEditForm(initial={'email':usuario.email})
    return render( request , "editar_perfil.html" , {"mi_formulario":mi_formulario , "usuario":usuario})


def about(request):

    return render ( request, "about.html")




