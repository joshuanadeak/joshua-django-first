from django.shortcuts import render
from wishlist.models import BarangWishlist

# Isi Views
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Joshua Mihai Daniel Nadeak'
    }
    return render(request, "wishlist.html", context)
    