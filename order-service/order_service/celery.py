from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery import bootsteps
from kombu import Consumer, Exchange, Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'order_service.settings')

my_queue = Queue('MsQueue', Exchange('MsExchange'))
app = Celery('order_service', broker ='amqp://order:12345@rabbitmq')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

from .mtasks import change_order_status

class MyConsumerStep(bootsteps.ConsumerStep):

    def get_consumers(self, channel):
        return [Consumer(channel,
                         queues=[my_queue],
                         callbacks=[self.handle_message],
                         accept=['json'])]

    def handle_message(self, body, message):
        print('Received message: {0!r}'.format(body))
        id_order = int(body['id'])
        status = body['status']
        # test.apply_async((id_order, status),
        change_order_status(id_order, status)
        message.ack()

app.steps['consumer'].add(MyConsumerStep)

