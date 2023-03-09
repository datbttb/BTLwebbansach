from django.shortcuts import render, redirect
from Category.models import Product, Category


def themsanpham(request):
    if request.method=='POST':
        loai=request.POST['theloai']
        product=Product.objects.create(name=request.POST['name'],slug=request.POST['slug'],price=request.POST['price'],image=request.FILES['image'],quantity=request.POST['so-luong'],description=request.POST['mo-ta'],publisher=request.POST['nha-cung-cap'])
        loai=Category.objects.get(slug=loai)
        product.categories.add(loai)
        product.save()
        return  redirect('/category/sanpham')
    else:
        return redirect('/')



def getform(request):
    category_list = Category.objects.all()
    return render(request, "Category/them.html", {"category_list": category_list})

def dssanpham(request):
    sanpham_list=Product.objects.all()
    return render(request, "Category/DanhSachSanPham.html", {"sanpham_list": sanpham_list})