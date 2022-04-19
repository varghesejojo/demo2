
from django.shortcuts import render
from .models import Place,Team
# Create your views here.

def demo(request):
    obj=Place.objects.all()
    obc=Team.objects.all()
    results={
        'result':obj,
        'res':obc,
    }
    return render(request, "index.html",results)

#def operation(request):
    #return render(request,'result.httml')