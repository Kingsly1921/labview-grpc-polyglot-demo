
# Python (grpcio)

```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install grpcio grpcio-tools
python -m grpc_tools.protoc -I ../proto --python_out=. --grpc_python_out=. ../proto/measurement.proto
```

See gRPC Python quickstart for more options. citeturn1search8
