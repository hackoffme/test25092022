from django.db import models


class Orders(models.Model):
    number = models.IntegerField(db_index=True,unique=True ,verbose_name='№ заказа')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    price_rub = models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2, verbose_name='Цена')
    delivery_time = models.DateField(verbose_name='Дата поставки')
    
    