from django.shortcuts import render
from .forms import InputForm


def formulario(request):

    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data.get('nome')
            email = form.cleaned_data.get('email')
            mensagem = form.cleaned_data.get('mensagem')
            form.save()
    form = InputForm()
    msg = 'Alguma mensagem'
    return render(request, 'myapp/formulario.html', {'form': form})



