from django.db import models
from django.forms.models import model_to_dict


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, verbose_name='Название товара')
    amount = models.IntegerField()
    price = models.FloatField()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return model_to_dict(self, fields=[field.name for field in self._meta.fields])

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        db_table = 'warehouse_items'
