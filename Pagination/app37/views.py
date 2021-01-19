from django.shortcuts import render,redirect
from .models import ProductModels
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def showIndex(request):
    result = ProductModels.objects.all()
    if result:
        return render(request,"index.html",{"data":result})
    else:
        return render(request,"index.html",{"error":"Product is not saved"})

def add_product_page(request):
    return render(request,"add_product_page.html")


def save_product(request):
    n = request.POST.get('p1')
    p = request.POST.get('p2')
    q = request.POST.get('p3')
    i = request.FILES['p4']
    c = request.POST.get('p5')
    ProductModels(name=n,price=p,quantity=q,image=i,category=c).save()
    messages.success(request,"Product Saved")
    return redirect('add_product_page')


def View_products(request):
    result = ProductModels.objects.all()
    p = Paginator(result,2)
    pno = request.GET.get("pageno",0)
    if pno == 0:
        page = p.page(1)
    else:
        page = p.page(pno)
    return render(request,"View_products.html",{"data":page})
