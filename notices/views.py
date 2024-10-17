from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'notices/pages/home.html')


def notice_details(request, id):
    return render(request, 'notices/pages/notice-view.html', context={
        'name': 'Renato Rocha',
    })
