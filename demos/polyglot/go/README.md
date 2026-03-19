
# Go

```bash
go mod init example.com/polyglot
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
protoc -I ../proto --go_out=. --go-grpc_out=. ../proto/measurement.proto
```

See gRPC Go quickstart. citeturn1search8
