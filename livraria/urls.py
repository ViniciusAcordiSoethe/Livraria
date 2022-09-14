"""livraria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path , include  

from core import views

from core.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', views.teste),
    path('pag2/' , views.teste2),
    path('categoriasteste/', views.CategoriaView.as_view(), name='todascategorias'),
    path('categoriateste/<int:pk>', views.CategoriaSoloView.as_view() , name='categoria'),
    path('criarcategoria/', views.criarcategoria , name='criarcategoria'),
    path('deletarcategoria/<int:id>', views.deletarCategoria, name='deletecategoria'),
    path('criaressacategoria', views.criaressacategoria, name='criaressacategoria' ),
    path('updatecategoria/<int:id>', views.updateCategoria, name= 'updatecategoria'),
    path('categorias-apiview/', views.CategoriasList.as_view(), name='categorias-apiview'),
    path('categorias-apiview/<int:pk>', views.CategoriaDetailView.as_view() , name='categorias-apiviewunica'),
    path('categorias-genericview/', views.CategoriasListCreateGeneric.as_view(), name='categorias-genericview'),
    path('categorias-genericview/<int:id>', views.CategoriaRetrieveUpdateDestroyGeneric.as_view() , name='categorias-genericupdate'),
    path('',include(router.urls))
]
