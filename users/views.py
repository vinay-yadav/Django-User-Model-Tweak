from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')


def session_end_check(request):
    print('logged out')
    return HttpResponse('success')