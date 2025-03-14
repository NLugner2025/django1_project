from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
# Create your views here.
def about_me(request):
    return HttpResponse("This would be the about page")