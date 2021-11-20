from django.shortcuts import render


def formulario(request):
    return render(request, 'myapp/formulario.html')
