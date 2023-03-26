from django.shortcuts import render,redirect
from .models import Aticle
from .forms import AticleForm


def news_home(request):
    news= Aticle.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news':news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = AticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'

    form=AticleForm()

    data = {
        'form':form
    }
    return render(request,'news/create.html',data)