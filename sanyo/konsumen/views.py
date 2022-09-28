from contextlib import redirect_stderr
from unicodedata import name
from django.shortcuts import render, redirect
from .models import Konsumen, Produk

# Create your views here.
def Index(request):
    return render(request, "index.html")

def Order(request):
    users = Produk.objects.all()
    return render(request, "order.html", {
        'jasa': users,
        'harga': users
    })
    # return render(request, "order.html")

def Service(request):
    return render(request, "service.html")

def Office(request):
    return render(request, "office.html")
    
def Create(request):
    konsumen = Konsumen()
    if request.method=="POST":
        konsumen.nama=request.POST.get('nama')
        konsumen.alamat=request.POST.get('alamat')
        konsumen.hp=request.POST.get('hp')
        konsumen.produk=Produk.objects.get(jasa=request.POST.get('produk'))
        konsumen.harga=request.FILES.get('bukti')
        konsumen.save()
    return redirect('/order')
