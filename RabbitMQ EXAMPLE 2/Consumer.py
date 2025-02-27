import pika, os

url = os.environ.get(
    'CLOUDAMQP_URL',
    'amqps://lezqtytn:8eZ7Lgav2Y_d3jn68VBkXuO6op2gM6uB@collie.lmq.cloudamqp.com/lezqtytn'
)
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

# Declare exchange correctly with exchange_type
channel.exchange_declare(exchange='text_exchange', exchange_type='direct')

# Declare queue
channel.queue_declare(queue='text_queue')

# Bind queue to exchange with correct routing key
channel.queue_bind(queue='text_queue', exchange='text_exchange', routing_key='texts')

# Publish message with matching routing key
channel.basic_publish(
    exchange='text_exchange',
    routing_key='texts',  # This must match the queue_bind routing key
    body='hello'
)

print('Message Received')

# Correctly close channel and connection
channel.close()
connection.close()
