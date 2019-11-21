from django.db import models
from django.forms.models import model_to_dict
from payment_service.models import PaymentStatus


class PaymentInfo(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    paymentStatus = models.CharField(max_length=10, choices=PaymentStatus.choices(), verbose_name='Статус заказа')

    def __unicode__(self):
        return self.order_id

    def __str__(self):
        return self.order_id

    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return model_to_dict(self, fields=[field.name for field in self._meta.fields])

    class Meta:
        verbose_name = 'Информация о платеже'
        verbose_name_plural = 'Информации о платежах'
        db_table = 'payment_info'
