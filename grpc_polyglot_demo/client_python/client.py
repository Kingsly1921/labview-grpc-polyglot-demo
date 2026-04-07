import grpc
import measurement_pb2
import measurement_pb2_grpc
import time
import numpy as np
import matplotlib.pyplot as plt


SERVER_ADDRESS = "localhost:50051"


def get_status(stub):
    response = stub.GetStatus(measurement_pb2.StatusRequest())
    print("✅ Server Status")
    print("   Time   :", response.server_time)
    print("   Version:", response.version)
    print()


def acquire_data(stub):
    response = stub.AcquireSensorData(
        measurement_pb2.DataRequest(sample_count=50)
    )
    data = np.array(response.values)
    print("✅ Acquired Data:", data[:5], "...")
    return data


def process_data(stub, data):
    response = stub.ProcessData(
        measurement_pb2.ProcessRequest(input_values=data.tolist())
    )
    print("✅ Processed Data")
    print("   RMS :", response.rms)
    print("   Avg :", response.average)
    print()


def plot_data(data):
    plt.plot(data)
    plt.title("Sensor Data from LabVIEW Server")
    plt.xlabel("Sample Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()


def stream_data(stub):
    print("✅ Streaming Data (Ctrl+C to stop)")
    stream = stub.StreamSensorData(
        measurement_pb2.StreamRequest(interval_ms=500)
    )

    try:
        for data_point in stream:
            print(
                f"Value: {data_point.value:.3f}, "
                f"Timestamp: {data_point.timestamp}"
            )
    except KeyboardInterrupt:
        print("\nStreaming stopped by user.")


def main():
    channel = grpc.insecure_channel(SERVER_ADDRESS)
    stub = measurement_pb2_grpc.MeasurementServiceStub(channel)

    get_status(stub)

    data = acquire_data(stub)
    process_data(stub, data)
    plot_data(data)

    stream_data(stub)


if __name__ == "__main__":
    main()