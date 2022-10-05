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
    livro  = CharField(source='livro.id')
    class Meta:
        model = ItensCompra
        fields = ('livro','quantidade')
        depth = 1
    


class CompraSerializer(ModelSerializer):
    usuario = CharField(source='usuario.id')
    itens = ItensCompraSerializer(many=True)
    class Meta:
        model = Compra
        fields = ('id','usuario', 'status' ,'itens' , 'total')


class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ('livro','quantidade')

class CriarEditarCompraSerializer(ModelSerializer):
    itens = CriarEditarItensCompraSerializer(many=True)
    class Meta:
        model = Compra
        fields = ('usuario','itens')

    def create(self, validated_data):
        itens = validated_data.pop('itens')
        compra = Compra.objects.create(**validated_data)
        for item in itens:
            ItensCompra.objects.create(compra=compra,**item)
        compra.save()
        return compra 

    def update(self, instance, validated_date):
        itens = validated_date.pop("itens")
        if itens:
            instance.itens.all().delete()
            for item in itens:
                ItensCompra.objects.create(compra=instance, **item)
            instance.save()
        return instance