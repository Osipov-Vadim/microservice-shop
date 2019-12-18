from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery import bootsteps
from kombu import Consumer, Exchange, Queue
from celery import shared_task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'payment_service.settings')

my_queue = Queue('MsQueue', Exchange('MsExchange'))

app = Celery('payment_service', broker ='amqp://payment:12345@rabbitmq')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@shared_task
def send_me_a_message(who, producer=None):
    with app.producer_or_acquire(producer) as producer:
        producer.publish(
            {'hello': who},
            serializer='json',
            exchange=my_queue.exchange,
            declare=[my_queue],
            retry=True,
        )