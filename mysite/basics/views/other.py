from django.shortcuts import render


def index(request):
    return render(request, 'basics/index.html')


def vuetest(request):
    return render(request, 'basics/vuetest.html')
