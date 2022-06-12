from django.shortcuts import render,redirect

from .models import Laptop
from .forms import LaptopForm
from django.core.paginator import Paginator,EmptyPage
from fpdf import FPDF
# Create your views here.

def LaptopView(request):
    form = LaptopForm()
    template_name='app/lapview.html'
    context={'form':form}
    if request.method=='POST':
        form=LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showlap_url')
    return render(request,template_name,context)

def ShowLaptop(request,page=1):
    data=Laptop.objects.all()
    template_name='app/showlap.html'
    paginator=Paginator(data,3)
    try:
        data=paginator.page(page)
    except:
        data=paginator.page(paginator.num_pages)
    context={'obj':data}
    return render(request,template_name,context)

def UpdateLaptopView(request,id):
    obj=Laptop.objects.get(id=id)
    form = LaptopForm(instance=obj)
    template_name='app/lapview.html'
    context={'form':form}
    if request.method=='POST':
        form = LaptopForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showlap_url')
    return render(request,template_name,context)

def DeleteLaptopView(request,id):
    obj=Laptop.objects.get(id=id)
    template_name='app/confirmation.html'
    
    if request.method=="POST":
        obj.delete()
        return redirect('showlap_url')
    context={'obj':obj}
    return render(request,template_name,context)
