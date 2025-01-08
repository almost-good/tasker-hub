from django.http import HttpResponse
from django.shortcuts import render



def test_connection(request):
    return HttpResponse('Connection successful!')
