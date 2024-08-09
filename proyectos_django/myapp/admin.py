from django.contrib import admin
from myapp.models import Person, Product, Carrito, ItemCarrito

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name"]
    search_fields = ["first_name", "last_name"]


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "product_name", "brand", "buy_price", "sell_price", "stock" ]
    search_fields = ["product_name", "brand"]
    list_filter = ["brand",]


admin.site.register(Person, PersonAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)