from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomersForm


def index(request):
    error = ''
    if request.method == 'POST':#МЕТОДИ ПЕРЕДАЧІ ІЗ ФОРМИ, ПЕРЕВІРКА ЧИ ФОРМА ЗАПОВНЕНА КОРЕКТНО ЯКЩО НІ ТО ПОМИЛКА
        form = CustomersForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            error = "Форма неправильна"


    form = CustomersForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/index.html', data)

def about(request):
    return HttpResponse("<h1>ABOUT</h1>")
