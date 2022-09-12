from rest_framework.serializers import ModelSerializer , CharField

from core.models import Categoria , Editora , Autor , Livro

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'


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
    class Meta:
        model = Livro
        fields = '__all__'
        depth= 1