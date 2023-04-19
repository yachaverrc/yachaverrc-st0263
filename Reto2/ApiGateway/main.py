import os
from flask import Flask, jsonify
import grpc
import sys
import pika
import uuid
from concurrent import futures
sys.path.append('../GRPC')
import file_service_pb2
import file_service_pb2_grpc

################################################################################################################

app = Flask(__name__)

grpc_channel = grpc.insecure_channel('localhost:50051')

file_service_client = file_service_pb2_grpc.FileServiceStub(grpc_channel)

################################################################################################################

mom_connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('user', 'password'))
)

mom_channel = mom_connection.channel()

result = mom_channel.queue_declare(queue = '', exclusive = True)
response_queue = result.method.queue
mom_channel.queue_bind(exchange = 'myExchange', queue = response_queue, routing_key = 'response')

################################################################################################################

@app.route('/list', methods = ['GET'])
def list_files():
    try:
        try:
            filenames = list_files_grpc()
            return jsonify(filenames)
        except: 
            filenames = list_files_mom()
            return jsonify(filenames)
    except:
        return "Error al obtener los archivos"
        

################################################################################################################
    

def list_files_grpc():
    request = file_service_pb2.ListFilesRequest()
    response = file_service_client.ListFiles(request)
    return list(response.filenames)


################################################################################################################

def search_files_grpc(filename):
    request = file_service_pb2.FileExistsRequest(filename = filename)
    response = file_service_client.FileExists(request)
    return response

################################################################################################################

@app.route('/search/<filename>', methods = ['GET'])
def file_exists(filename):
    try: 
        try:
            response = search_files_grpc(filename)
            print(response)
            if response.exists:
                return f'El archivo {filename} existe.', 200
            else: 
                return f'El archivo {filename} no existe.', 404
        except:
            response = find_files_mom(filename)
            if response == "False":
                return f'El archivo {filename} existe.', 200
            else:
                return f'El archivo {filename} no existe.', 400
    except:     
        return "Error al buscar archivos", 500  

    

################################################################################################################

def list_files_mom():

    print("Consultando Archivos en Sistema")

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials("user", "password")))
    channel = connection.channel()

    channel.basic_publish(exchange = 'myExchange', routing_key = 'request', body = 'list')

    method_frame, header_frame, body = channel.basic_get(queue = 'response', auto_ack = True)
    while method_frame is None:
        method_frame, header_frame, body = channel.basic_get(queue ='response', auto_ack = True)

    response = {'message': body.decode('utf-8')}

    return response

################################################################################################################


def find_files_mom(name):

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials("user", "password")))
    channel = connection.channel()

    channel.basic_publish(exchange = 'myExchange', routing_key = 'request', body = 'find/'+name)

    method_frame, header_frame, body = channel.basic_get(queue = 'response', auto_ack = True)

    while method_frame is None:
        method_frame, header_frame, body = channel.basic_get(queue = 'response', auto_ack = True)

    response = body.decode('UTF-8')

    return response


if __name__ == '__main__':
    app.run()

