from django.shortcuts import render


def index(request):
    title = 'Магазин'
    context = {
        'title': title,
    }
    return render(request, 'geekshop/index.html', context=context)


def contacts(request):
    title = 'Контакты'
    context = {
        'title': title,
    }
    return render(request, 'geekshop/contact.html', context=context)
