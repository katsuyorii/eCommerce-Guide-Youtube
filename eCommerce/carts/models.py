from django.db import models
from users.models import User
from goods.models import Product

class CartQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        
        return 0
\
class Cart(models.Model):
    user = models.ForeignKey(to=User, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Пользователь:")
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name="Товар:")
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Количество:")
    session_key = models.CharField(max_length=32, blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления:")

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    objects = CartQueryset.as_manager()

    def __str__(self):
        return f'Корзина {self.user.username} | Товар { self.product.name } | Количество { self.quantity }'
    
    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)
 