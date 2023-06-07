from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from .models import Team

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'abc':obj1})
# def addition(request):
#     x=int(request.GET['num1'])
#     Y=int(request.GET['num2'])
#     res=x+Y
#     ab=x/Y
#     abc=x-Y
#     abcd=x*Y
#     return render(request,"about.html",{'result':res,'anb':ab,'sub':abc,'mul':abcd})
# def about(request):
#     return render(request,"about.html")
# def hai(request):
#     return HttpResponse('hai abhinav')