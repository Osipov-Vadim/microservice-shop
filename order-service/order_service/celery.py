from __future__ import absolute_import, unicode_literals
import os
import django
from celery import Celery
from celery import bootsteps
from kombu import Consumer, Exchange, Queue
# from kombu.utils.functional import reprcall

from django.http import HttpResponse, HttpResponseServerError
from django.http.response import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'order_service.settings')

my_queue = Queue('MsQueue', Exchange('MsExchange'))
app = Celery('order_service', broker ='amqp://order:12345@rabbitmq')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

my_queue = Queue('MsQueue', Exchange('MsExchange'))


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    return
    #Calls test('hello') every 10 seconds.
    # sender.add_periodic_task(10.0, test('hello'), name='add every 10')

    # # Calls test('world') every 30 seconds
    # sender.add_periodic_task(30.0, test('world'), expires=10)


# class MyConsumerStep(bootsteps.ConsumerStep):

#     def get_consumers(self, channel):
#         return [Consumer(channel,
#                          queues=[my_queue],
#                          callbacks=[self.handle_message],
#                          accept=['json'])]

#     def handle_message(self, body, message):
#         print('Received message: {0!r}'.format(body))
#         # id_order = int(body['id'])
#         # fun = body['fun']
#         # reprcall(fun.__name__)
#         message.ack()
#         # change_order_status(id_order, "PAID")

# # app.steps['consumer'].add(MyConsumerStep)

