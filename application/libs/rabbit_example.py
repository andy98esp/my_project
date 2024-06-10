import os

import pika


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


def receive_results():
    credentials = pika.PlainCredentials(os.getenv('RABBITMQ_DEFAULT_USER'), os.getenv('RABBITMQ_DEFAULT_PASS'))
    parameters = pika.ConnectionParameters('rabbitmq', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # Declara la cola sin especificar propiedades adicionales
    channel.queue_declare(queue='tasks-queue')

    channel.basic_consume(queue='tasks-queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    receive_results()
