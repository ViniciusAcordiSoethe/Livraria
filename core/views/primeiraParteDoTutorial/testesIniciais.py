from django.http import HttpResponse

def teste(request):
    return HttpResponse("Olá Mundo do Django")

def teste2(request):
    return HttpResponse("teste 2")