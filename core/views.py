from django.http import HttpResponse , JsonResponse
from django.views import View , generic
from django.views.decorators.csrf import csrf_exempt
from core.models import Categoria
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator

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


    # def get(self, request , id=None):
    #     if id:
    #         qs = Categoria.objects.get(id=id)
    #         data = {}
    #         data['id'] = qs.id
    #         data['descricao'] = qs.descricao
    #         return JsonResponse(data)
    #     else:
    #         data = list(Categoria.objects.values())
    #         formatted_data = json.dumps(data , ensure_ascii=False)
    #         return HttpResponse(formatted_data, content_type="application/json")
    # def post(self , request):
    #     json_data = json.loads(request.body)
    #     nova_categoria = Categoria.objects.create(**json_data)
    #     data = {"id": nova_categoria.id, "descricao": nova_categoria.descricao}
    #     return JsonResponse(data)/categoria/1