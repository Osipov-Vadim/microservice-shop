from django.db import models
from django.forms.models import model_to_dict
from order_service.models.order_status import OrderStatus


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=120, verbose_name='Имя')
    status = models.CharField(max_length=10, choices=OrderStatus.choices(), verbose_name='Статус заказа')
    totalCost = models.FloatField(default=0.0)
    totalAmount = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return model_to_dict(self, fields=[field.name for field in self._meta.fields])

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        db_table = 'orders'
