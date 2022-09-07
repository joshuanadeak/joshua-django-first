from django.db import models

# Models for The Wishlist
class BarangWishlist(models.Model):
    nama_barang = models.CharField(max_length=50)
    harga_barang = models.IntegerField()
    deskripsi = models.TextField()