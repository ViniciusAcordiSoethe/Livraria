from rest_framework import routers

from core import views

router = routers.DefaultRouter()
router.register(r'categorias' , views.CategoriaViewSet)
router.register(r'editoras' , views.EditoraViewSet)
router.register(r'autores' , views.AutorViewSet)
router.register(r'livros' , views.LivroViewSet)
router.register(r'compras', views.CompraViewSet)