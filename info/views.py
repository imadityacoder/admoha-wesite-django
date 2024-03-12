from django.shortcuts import render,HttpResponse

# Create your views here.
def info_home(request):
    return HttpResponse("info page")