from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum

from book.models import Book
from clothes.models import Clothes
from mobile.models import Mobile

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cart'
        verbose_name = 'Cart'


class CartItem(models.Model):
    product_id = models.CharField(max_length=255)
    quantity = models.IntegerField()
    type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')

    def __str__(self):
        return self.product_id
    class Meta:
        db_table = 'cart_item'
        verbose_name = 'CartItem'
    def save(self, *args, **kwargs):
        if self.product_id[0] == 'B':
            self.type= 'Book'
            self.price = Decimal(str(Book.objects.get(id=self.product_id).price))
            # chuyển từ Decimal128(MongoDB) sang Decimal(MySQL)
        elif self.product_id[0] == 'M':
            self.type = 'Mobile'
            self.price = Decimal(str(Mobile.objects.get(id=self.product_id).price))
        elif self.product_id[0] == 'C':
            self.type = 'Clothes'
            self.price = Decimal(str(Clothes.objects.get(id=self.product_id).price))
        super(CartItem, self).save(*args, **kwargs)

