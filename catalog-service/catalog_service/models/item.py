from django.db import models
from django.forms.models import model_to_dict
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
import time


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, verbose_name='Название товара')
    amount = models.IntegerField(default=0)
    price = models.FloatField()

    def change_amount(self, shift: int):
        self.amount += shift
        time.sleep(4)
        self.save()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.clean()
        super().save(force_insert, force_update, using, update_fields)

    def clean(self):
        if self.amount < 0:
            raise ValidationError(_('The quantity of items must be at least 0'))
        if self.price < 0.0:
            raise ValidationError(_('The price of items must be at least 0'))

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return model_to_dict(self, fields=[field.name for field in self._meta.fields])

    class Meta:
        # models.CheckConstraint(check=models.Q(amount__gte=0), name='amount_gte_0')
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        db_table = 'warehouse_items'


class CreateItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'amount', 'price']

    def create(self, validated_data):
        item = Item(
            name=validated_data['name'],
            amount=validated_data['amount'],
            price=validated_data['price']
        )
        item.save()
        return item
