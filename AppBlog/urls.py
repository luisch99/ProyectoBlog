from django.urls import path
from .views import *
from AppBlog import views
from django.contrib.auth.views import LogoutView
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('inicio/', inicio, name='Inicio'),
    path('detalle/', detalle, name='detalle'),
    path('contactenos/', contactenos, name='contactenos'),
    path('nosotros/', nosotros, name='nosotros'),
    path('obligacion/', logueate, name='obligacion'),
#---------------------------------------------------------------------------------
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='AppBlog/logout.html'), name='logout'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),
]

handler404 = Error404View.as_view()