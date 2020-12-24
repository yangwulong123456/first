from django.shortcuts import render
from django.http import HttpResponse
from book.models import BookInfo

# Create your views here.
def index(request):
    return HttpResponse('ok!')

