from django.db import models

class Kategori(models.Model):
    kategori=models.CharField(max_length=30,default=None)
    def __str__(self) -> str:
        return self.kategori

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    kategoriler=models.ForeignKey(Kategori,on_delete=models.CASCADE,null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='', blank=True, null=True)

    def __str__(self):
        return self.name

