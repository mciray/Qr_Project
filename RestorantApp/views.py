from django.shortcuts import render
from .models import Product,Kategori
# Create your views here.
def urunler(request):
    urun = Product.objects.all()
    kategoriler = Kategori.objects.all()    
    
    return render(request,"Urunpage.html",{'urun':urun,'kategoriler':kategoriler})

def kategori(request,kategoriId):
    context={}
    kategori=Product.objects.filter(kategoriler__id=kategoriId)
    context['kategorigit']=kategori
    return render(request,"kategori.html",context)


