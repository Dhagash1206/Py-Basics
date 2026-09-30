import grpc
import greeter_pb2
import greeter_pb2_grpc

with grpc.insecure_channel("localhost:50051") as channel:
    stub = greeter_pb2_grpc.GreeterStub(channel)
    print(stub.SayHello(greeter_pb2.HelloRequest(name="Asha")).message)
    for streamed_reply in stub.StreamGreetings(greeter_pb2.HelloRequest(name="Asha")):
        print(streamed_reply.message)
