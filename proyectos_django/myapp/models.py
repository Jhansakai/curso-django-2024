from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    document_number = models.CharField(max_length=10, null=True, blank=True, default='')

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
    

class Product(models.Model):
    product_name = models.CharField(max_length=80)
    brand = models.CharField(max_length=80)
    description = models.TextField() #large texts
    buy_price = models.IntegerField()
    sell_price = models.IntegerField()
    stock = models.IntegerField()
    inventario = models.IntegerField()

    def __str__(self):
        return f"{self.product_name}"


class Carrito(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, default=None, null=True, blank=True)
    name = models.CharField(max_length=128)
    productos = models.ManyToManyField(Product, through="ItemCarrito")

    def __str__(self):
        return self.name

class ItemCarrito(models.Model):
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return "{} {} {}".format(self.carrito.name, self.producto.product_name,  self.cantidad)