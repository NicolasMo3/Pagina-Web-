"""
URL configuration for mi_crm project.

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
from django.contrib.auth import views as auth_views  # Importa las vistas de autenticación
from crm import views
from crm.views import encuesta

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/profile/', views.dashboard, name='dashboard'),  # Redirige a la nueva vista del dashboard
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/add/', views.add_cliente, name='add_cliente'),  # Nueva URL para añadir cliente
    path('', views.home, name='logout'),
    path('encuesta/', encuesta, name='encuesta'),
]

