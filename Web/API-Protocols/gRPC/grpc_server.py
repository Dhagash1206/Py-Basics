# gRPC: binary Protobuf over HTTP/2, strongly typed contract.
# Setup: python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. greeter.proto
# Run:   python grpc_server.py
import time
from concurrent import futures
import grpc
import greeter_pb2
import greeter_pb2_grpc


class GreeterService(greeter_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return greeter_pb2.HelloReply(message=f"Hello, {request.name}!")

    def StreamGreetings(self, request, context):
        for greeting_index in range(3):
            yield greeter_pb2.HelloReply(message=f"Greeting {greeting_index + 1} for {request.name}")
            time.sleep(0.5)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    greeter_pb2_grpc.add_GreeterServicer_to_server(GreeterService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("gRPC server on :50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
