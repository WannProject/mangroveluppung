from django.db import models
from django.core.validators import URLValidator

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField() 
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.title

    
# todo landing page aplication

class DestinationItem(models.Model):
    image = models.ImageField(upload_to='destinations/', help_text="Gambar destinasi")
    deskripsi = models.CharField(max_length=100, help_text="Lokasi destinasi")

    def __str__(self):
        return self.deskripsi

    class Meta:
        verbose_name = "Item Destinasi"
        verbose_name_plural = "Item-item Destinasi"

# todo UMKM
class UMKMProduct(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nama Produk")
    image = models.ImageField(upload_to='umkm_products/', verbose_name="Gambar Produk")
    price = models.CharField(max_length=20, verbose_name="Harga")  # Mengubah DecimalField menjadi CharField
    shopee_link = models.URLField(validators=[URLValidator()], verbose_name="Link Shopee")

    def __str__(self):
        return f"{self.name} - {self.price}"

    class Meta:
        verbose_name = "Produk UMKM"
        verbose_name_plural = "Produk-produk UMKM"