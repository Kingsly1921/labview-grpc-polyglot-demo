
# C# (.NET)

```bash
dotnet new console -n PolyglotClient
cd PolyglotClient
dotnet add package Grpc.Net.Client
dotnet add package Grpc.Tools
# Add <Protobuf Include="..\proto\measurement.proto" GrpcServices="Client" /> to .csproj
```

Method types overview (unary/streaming) on Microsoft Learn. citeturn1search9
