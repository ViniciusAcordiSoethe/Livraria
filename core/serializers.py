from rest_framework.serializers import ModelSerializer , CharField , SerializerMethodField

from core.models import Categoria, Compra , Editora , Autor , Livro , ItensCompra

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'

class EditoraNestedSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = ('nome',)
class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class LivroDetailSerializer(ModelSerializer):
    categoria = CharField(source='categoria.descricao')
    editora = EditoraNestedSerializer() # sem usar a profundidade so usar o serializer normal
    autores = SerializerMethodField() #função do django
    class Meta:
        model = Livro
        fields = '__all__'
        depth= 1 # usando profundidade porem exibe o id 

    def get_autores(self,obj):
        nome_autores = []
        autores = obj.autores.get_queryset()
        for autor in autores:
            nome_autores.append(autor.nome)
        return nome_autores

class ItensCompraSerializer(ModelSerializer):
    livro  = CharField(source='livro.titulo')
    class Meta:
        model = ItensCompra
        fields = ('livro','quantidade')
        depth = 1
    


class CompraSerializer(ModelSerializer):
    usuario = CharField(source='usuario.email')
    itens = ItensCompraSerializer(many=True)
    class Meta:
        model = Compra
        fields = ('id','usuario','itens' , 'total')

