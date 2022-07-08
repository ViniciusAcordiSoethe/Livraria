from click import pass_context
from django.http import HttpResponse , JsonResponse
from django.views import View , generic
from django.views.decorators.csrf import csrf_exempt
from yaml import serialize
from core.models import Categoria
from django.shortcuts import redirect, render , get_object_or_404
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from rest_framework import status

from .forms import CategoriaForm

import json
# Create your views here.

def teste(request):
    return HttpResponse("Olá Mundo do Django")

def teste2(request):
    return HttpResponse("teste 2")

@method_decorator(csrf_exempt , name="dispatch")
class CategoriaView(generic.ListView):
    template_name = "core/categorias.html"
    context_object_name = 'latest_categoria_list'

    def get_queryset(self):
        return Categoria.objects.all()

# @method_decorator(csrf_exempt , name="dispatch")
class CategoriaSoloView(generic.DetailView):
    model = Categoria
    template_name= 'core/detalhes.html'

def criarcategoria(request):
    form = CategoriaForm()
    context = {
        'form':form
    }
    return HttpResponse(render(request , 'core/criarcategoria.html' , context=context))

def criaressacategoria(request):
    form = CategoriaForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/categorias')
    else:
        return redirect('/categorias')

def deletarCategoria(request , id):
    categoria = get_object_or_404(Categoria, pk=id)
    categoria.delete()
    return redirect('/categorias')

def updateCategoria(request, id ):
    if request.method == 'GET':
        categoria = Categoria.objects.filter(id=id).first()
        form = CategoriaForm(instance=categoria)

        context= {
            'categoria': categoria,
            'form':form
        }
        return render(request , 'core/editarcategoria.html' , context=context)

    elif request.method == 'POST':
        categoria = Categoria.objects.filter(id=id).first()
        form = CategoriaForm(request.POST, instance=categoria)

        if form.is_valid():
            form.save()
            return redirect('/categorias')
        else:
            return redirect('/categorias')


    
    # def get(self, request , id=None):
    #     if id:
    #         qs = Categoria.objects.get(id=id)
    #         data = {}
    #         data['id'] = qs.id
    #         data['descricao'] = qs.descricao
    #         return JsonResponse(data)
    #     else:
    #         data = list(Categoria.objects.values())
    #         formatted_data = json.dumps(data , ensure_ascii=False)dmin/core/categoria/
    #     data = {"id": nova_categoria.id, "descricao": nova_categoria.descricao}
    #     return JsonResponse(data)/categoria/1$ 289,49

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class CategoriasList(APIView):
    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriaDetailView(APIView):
    def get(self, request, pk):
        categoria = get_object_or_404(Categoria.objects.all(), id=pk)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)
    
    def put(self, request, pk):
        categoria = get_object_or_404(Categoria.objects.all(), id=pk)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        categoria = get_object_or_404(Categoria.objects.all(), id=pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)