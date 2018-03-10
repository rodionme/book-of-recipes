from django.shortcuts import render
from django.http import HttpResponse


def index(request, app):
    return HttpResponse('Hello ' + app['name'] + '!')
