from django.shortcuts import render

from MTVCoderApp.models import Familiar

# Create your views here.

def inicio(request):
      
    return render(request, "MTVCoderApp\index.html",{'familiares':familiares})


def familiares(request):
    
    familiares = Familiar.objects.all()
      
    return render(request,r"MTVCoderApp\familiares.html",{'familiares':familiares})