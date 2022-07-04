from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path("", views.inicio, name="inicio"),
    path("productos" , views.productos, name="productos"),
    path("alta_productos" , views.productos_formulario),
    path("buscar_producto" , views.buscar_producto),
    path("resultado_busqueda" , views.resultado_productos),
    path("datos" , views.datos, name="datos"),
    path("alta_datos" , views.datos_formulario),
    path("proveedores" , views.proveedores, name="proveedores"),
    path("alta_proveedores" , views.proveedores_formulario),
    path("elimina_producto/<int:id>" , views.elimina_producto , name="elimina_producto"),
    path("elimina_datos/<int:id>" , views.elimina_datos , name="elimina_datos"),
    path("elimina_proveedores/<int:id>" , views.elimina_proveedores , name="elimina_proveedores"),
    path("modificar_producto/<int:id>)", views.modificar_producto , name="modificar_producto"),
    path("modificar_producto/", views.modificar_producto , name="modificar_producto"),
    path("modificar_dato/<int:id>)", views.modificar_dato , name="modificar_dato"),
    path("modificar_dato/", views.modificar_dato , name="modificar_dato"),
    path("modificar_proveedores/<int:id>)", views.modificar_proveedores , name="modificar_proveedores"),
    path("modificar_proveedores/", views.modificar_proveedores , name="modificar_proveedores"),
    path("login" , views.login_request , name="Login"),
    path("registro" , views.registro , name="registro"),
    path("logout" , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path("editar_perfil" , views.editar_perfil , name="editar_perfil"),
    path("about" , views.about , name="About")
]
