from django.contrib import admin

from core.models import Categoria, Comentario , Editora , Autor , Livro , Compra , StatusCompra , ItensCompra
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['descricao']
class LivroAdmin(admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ('id', 'titulo' , 'preco')
class ItensInline(admin.TabularInline):
    model = ItensCompra
    extra = 3

class StatusCompraAdmin(admin.ModelAdmin):
    list_display= ('id','tipo')
class ComprasAdmin(admin.ModelAdmin):
    inlines= (ItensInline,)
    list_display= ('id' , 'usuario' , 'status')

class ComentarioAdmin(admin.ModelAdmin):
    list_display=('id', 'conteudoComentario')
    search_fields= ['conteudoComentario']

admin.site.register(Autor)
admin.site.register(Categoria , CategoriaAdmin)
admin.site.register(Editora)
admin.site.register(Comentario , ComentarioAdmin)
admin.site.register(Livro , LivroAdmin)
admin.site.register(Compra , ComprasAdmin)
admin.site.register(StatusCompra , StatusCompraAdmin)


