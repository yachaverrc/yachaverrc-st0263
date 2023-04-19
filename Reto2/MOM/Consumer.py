import pika
import os

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials("user", "password")))
channel = connection.channel()

def process_request(ch, method, props, body):
    message = body.decode('utf-8')

    archivo = message.split('/')

    print('mensaje recibido: ' + archivo[0])

    response_message = ""

    if archivo[0] == 'list':
        dir = os.listdir('../files')
        response_message = ';'.join(dir)

    if archivo[0] == 'find':
        filename = archivo[1] 
        exists = os.path.isfile(f'../files/{filename}')
        response_message = str(exists)

    print(response_message)

    channel.basic_publish(exchange = 'myExchange', routing_key = 'response',
                          properties = pika.BasicProperties(correlation_id = props.correlation_id), body = response_message.encode())


channel.basic_consume(queue = 'request', on_message_callback=process_request, auto_ack=True)
channel.start_consuming()
connection.close()



