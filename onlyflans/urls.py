"""
URL configuration for onlyflans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from web.views import *




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'Inicio'),
    path('acerca/', about, name = 'AcercaDe'),
    path('bienvenido/', welcome, name='Bienvenida'),
    path('crear-producto/', nuevo_producto, name='NuevoProducto'),
    path('detalle-producto/<slug:slug>/', detalle_producto, name="DetalleProducto"),
    path('detalle-producto/', lista_productos, name="ListaProducto"),
    path('contacto/', contact_view, name='contacto'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('info/<uuid:producto_id>/', vista_producto, name='detalle'),
    path('eliminar/<uuid:producto_id>/', eliminar_producto, name='EliminarProducto'),
    path('editar/<uuid:producto_id>/', editar_producto, name='EditarProducto'),
    path('filtro/', filtrar, name='filtro'),
    path('filtroproductos/', filtrar2, name='FiltroListaProductos'),
    path('filtrousuarios/', filtrarUsuarios, name='FiltroUsuarios'),
    path('cargar/', carga_masiva, name='Importar'),
    path('registro/', nuevo_usuario, name='NuevoUsuario'),
    path('editar-usuario/<int:usuario_id>/', editar_usuario, name='EditarUsuario'),
    path('eliminar-usuario/<int:usuario_id>/', eliminar_usuario, name='EliminarUsuario'),
    path('usuarios/', lista_usuarios, name="ListaUsuarios" ),
    path('ficha/<int:usuario_id>/', vista_ficha, name='Ficha'),
    path('carrito/agregar/<uuid:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', ver_carrito, name='VerCarrito'),
    path('pedido/', realizar_pedido, name='RealizarPedido'),
    path('vaciar/', vaciar_carrito, name='VaciarCarrito'),
    path('carrito/eliminar/<int:elemento_id>/', eliminar_item_carrito, name='EliminarLinea'),
    path('carrito/aumentar/<int:elemento_id>/', aumentar_item, name='AumentarCantidad'),
    path('carrito/disminuir/<int:elemento_id>/', disminuir_item, name='DisminuirCantidad'),
    path('historial-pedidos/', historial, name='HistorialPedidos')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

