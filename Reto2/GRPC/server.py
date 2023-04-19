import os
import grpc
import file_service_pb2
import file_service_pb2_grpc
from concurrent import futures

class FileServicer(file_service_pb2_grpc.FileServiceServicer):
    def ListFiles(self, request, context):

        dir = os.listdir('../files')
        res = file_service_pb2.ListFilesResponse(filenames = dir)   
        return res

    def FileExists(self, request, context):

        filename = request.filename
        exists = os.path.isfile(f'../files/{filename}')
        res = file_service_pb2.FileExistsResponse(exists = exists)
        return res

def serve():
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
    file_service_pb2_grpc.add_FileServiceServicer_to_server(FileServicer(), server)

    server.add_insecure_port('[::]:50051')
    server.start()

    print('Hola: Soy el servicio GRPC.')
    print('Starter in http://localhost:50051')

    server.wait_for_termination()

if __name__ == '__main__':
    serve()
