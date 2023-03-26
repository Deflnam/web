from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some','Hi','112'],
        'obj': {
            'car':'BMW',
            'age':17,
            'hobby':'football'
        }
    }
    return render(request,'main/index.html',data)


def about(request):
    return render(request,'main/about.html')
