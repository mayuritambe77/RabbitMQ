import pika,os

url=os.environ.get('CLOUDAMQP_URL','amqps://lezqtytn:8eZ7Lgav2Y_d3jn68VBkXuO6op2gM6uB@collie.lmq.cloudamqp.com/lezqtytn')
params=pika.URLParameters(url)
connection=pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare('text_exchange')
channel.queue_declare(queue='text_queue')
channel.queue_bind('text_queue','text_exchange','texts')

channel.basic_publish(
    body='hello',
    exchange='text_exchange',
    routing_key='tests'
)
print('msg sent')
channel.close
connection.close
