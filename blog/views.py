from django.http import HttpResponse
from django.shortcuts import render


def posts_list(request):
    names = ['Doniyor', 'Zarif', 'Zafar', 'Asad']
    return render(request, 'blog/index.html', context={'names': names})
