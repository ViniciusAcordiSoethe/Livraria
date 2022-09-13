from rest_framework.serializers import ModelSerializer , CharField , SerializerMethodField

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
    editora = EditoraSerializer() # sem usar a profundidade 
    autores = SerializerMethodField()
    class Meta:
        model = Livro
        fields = '__all__'
        depth= 1

    def get_autores(self,obj):
        nome_autores = []
        autores = obj.autores.get_queryset()
        for autor in autores:
            nome_autores.append(autor.nome)
        return nome_autores