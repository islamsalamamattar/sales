from locale import locale_encoding_alias
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django import template
from .models import *

# Create your views here.
@login_required
def index(request):
    context_object_name = 'index'
    context={}
    html_template = loader.get_template( 'frontend/index.html' )
    return HttpResponse(html_template.render(context, request))