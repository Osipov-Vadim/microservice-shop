from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery import bootsteps
from kombu import Consumer, Exchange, Queue


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'order_service.settings')

my_queue = Queue('MsQueue', Exchange('MsExchange'))

app = Celery('order_service', broker ='amqp://order:12345@192.168.99.101:5672')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

class MyConsumerStep(bootsteps.ConsumerStep):

    def get_consumers(self, channel):
        return [Consumer(channel,
                         queues=[my_queue],
                         callbacks=[self.handle_message],
                         accept=['json'])]

    def handle_message(self, body, message):
        print('Received message: {0!r}'.format(body))
        message.ack()
app.steps['consumer'].add(MyConsumerStep)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))