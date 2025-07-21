# gRPC client at agent
import grpc
import communication.grpc_interface_pb2 as pb2
import communication.grpc_interface_pb2_grpc as pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = pb2_grpc.TrainerServiceStub(channel)
    response = stub.TrainModel(pb2.TrainRequest(
        model_name="resnet",
        dataset_path="/data/cifar10",
        epochs=10,
        batch_size=32
    ))
    print(f"Training Status: {response.status}, Accuracy: {response.accuracy}")

if __name__ == "__main__":
    run()
