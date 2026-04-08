package main

import (
	"context"
	"log"

	pb "client_go/measurement"

	"google.golang.org/grpc"
)

func main() {

	// 1. Connect to LabVIEW gRPC server
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("❌ Failed to connect: %v", err)
	}
	defer conn.Close()

	client := pb.NewMeasurementServiceClient(conn)

	// 2. GetStatus call
	status, err := client.GetStatus(context.Background(), &pb.StatusRequest{})
	if err != nil {
		log.Fatalf("❌ GetStatus failed: %v", err)
	}

	log.Println("Server Time:", status.ServerTime)
	log.Println("Version    :", status.Version)

	// 3. AcquireSensorData
	dataResp, err := client.AcquireSensorData(
		context.Background(),
		&pb.DataRequest{SampleCount: 10},
	)
	if err != nil {
		log.Fatalf("❌ AcquireSensorData failed: %v", err)
	}

	log.Println("Sensor Data:", dataResp.Values)

	// 4. StreamSensorData
	log.Println("🔄 Streaming data from LabVIEW...")

	stream, err := client.StreamSensorData(
		context.Background(),
		&pb.StreamRequest{IntervalMs: 500},
	)
	if err != nil {
		log.Fatalf("❌ StreamSensorData error: %v", err)
	}

	for i := 0; i < 5; i++ {
		dp, err := stream.Recv()
		if err != nil {
			log.Fatalf("❌ Stream read error: %v", err)
		}
		log.Printf("Value: %.3f   Timestamp: %d\n", dp.Value, dp.Timestamp)
	}

	log.Println("✔ Go client finished")
}
