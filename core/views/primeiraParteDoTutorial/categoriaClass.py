from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from django.utils.decorators import method_decorator
from django.views import View , generic
from django.shortcuts import redirect, render , get_object_or_404

from core.models import Categoria
import json

from core.forms import CategoriaForm

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
