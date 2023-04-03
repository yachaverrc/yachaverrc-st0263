############################################3

import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials("user", "password")))
channel = connection.channel()

def callback(ch, method, properties, body):
    print(f'{body} is received')
    channel.close()
    exit()    

channel.basic_publish(exchange='myExchange', routing_key='request', body='Hello')
        
channel.basic_consume(queue="response", on_message_callback=callback, auto_ack=True)
channel.start_consuming()





