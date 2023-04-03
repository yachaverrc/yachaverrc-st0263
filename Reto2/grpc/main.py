import os
from flask import Flask, jsonify
import grpc
import sys
sys.path.append('../')
import greeting_pb2
import greeting_pb2_grpc

app = Flask(__name__)

@app.route("/", methods =['GET'])
def hello():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greeting_pb2_grpc.GreeterStub(channel) 
        try:
            response = stub.greet(greeting_pb2.ClientInput(greeting = "hola"))
            print("Greeter client received following from server: " + response.message)
        except Exception as e:
            return str(e)

    return response.message 

@app.route('/files', methods=['GET'])
def list_files():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greeting_pb2_grpc.FileServiceStub(channel)
        try:  
            request = greeting_pb2.ListFilesRequest()
            response = greeting_pb2.ListFilesResponse(request)
            filenames = list(response.filenames)
            return jsonify(filenames)      
        except Exception as e:
            return str(e)
    

if __name__ == '__main__':
    app.run(debug=True,port=4000)

