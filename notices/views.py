from django.shortcuts import render
from django.http import HttpResponse

from utils.notices.factory import make_notice


def home(request):
    return render(request, 'notices/pages/home.html', context={
        'notices': [make_notice() for _ in range(10)]
    })


def notice_details(request, id):
    return render(request, 'notices/pages/notice-view.html', context={
        'notice': make_notice(),
        'is_detail_page': True,
    })
