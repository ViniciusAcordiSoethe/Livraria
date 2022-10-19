from django.contrib import admin
from django.urls import path , include  

from core import views

from core.routers import router

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    #outros EndPoints     
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
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
    path('api/',include(router.urls))
]
