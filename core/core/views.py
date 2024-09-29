from django.shortcuts import render, redirect
from posts.models import DestinationItem, UMKMProduct

def homepage(request):
    destination_items = DestinationItem.objects.all()
    products = UMKMProduct.objects.all()  # Ambil data produk UMKM
    

    
    context = {
        'destination_items': destination_items,
        'products': products,  # Tambahkan produk UMKM ke dalam konteks
    }
    return render(request, 'index.html', context)
