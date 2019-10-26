from django.db import models
from django.forms.models import model_to_dict
from order_service.models.order import Order


class ReservedItem(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_id = models.IntegerField()
    amount = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return model_to_dict(self, fields=[field.name for field in self._meta.fields])

    class Meta:
        verbose_name = 'Зарезервированный товар'
        verbose_name_plural = 'Зарезервированные товары'
        db_table = 'reserved_items'
