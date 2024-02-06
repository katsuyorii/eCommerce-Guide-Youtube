from django.db import models
from users.models import User
from goods.models import Product

class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="Пользователь:")
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name="Товар:")
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Количество:")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления:")

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return f'Корзина {self.user.username} | Товар { self.product.name } | Количество { self.quantity }'

