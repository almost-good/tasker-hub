from django.shortcuts import render
from django.http import HttpResponse



def test_connection(request):
    return HttpResponse('Connection successful!')
