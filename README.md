# LabVIEW gRPC – Prototypes & Polyglot Demo

This repository contains two parts:

1. **`/prototypes`** – Minimal LabVIEW-first examples that cover **all RPC types** supported by gRPC (unary, server streaming).
2. **`/demos/polyglot`** – End-to-end demo for your talk **_“Building Scalable Multi‑Language Frameworks Using gRPC”_**, showing LabVIEW working with Python, C#, Node.js, and Go clients/servers using a shared `.proto` contract.

> Built around NI’s **grpc-labview** project and the official gRPC docs. See references at the end.

---

## Repository Map

```
labview-grpc-polyglot-demo/
  ├─ prototypes/
  │   ├─ proto/                     # Shared .proto contracts for prototype services
  │   ├─ unary/                     # Simple request/response
  │   ├─ server_streaming/          # Server stream (progress/events)
  │   ├─ multiple_streaming/        # Client stream (batch upload)
  │
  └─ demos/
      └─ polyglot/
          ├─ proto/                 # Canonical .proto for the demo service
          ├─ labview/               # LabVIEW server/client projects (placeholders)
          ├─ python/                # Python client or server
          ├─ csharp/                # .NET client or server
          ├─ nodejs/                # Node.js client or server
          └─ go/                    # Go client or server
```

---

## Quick Start (Top Level)

1. **Clone & set up tools**
   - Install **LabVIEW gRPC Library** using **VIPM** (LabVIEW 2019+).
   - Install language SDKs for gRPC in Python/.NET/Node/Go as needed (see language folders below). See gRPC introduction for background.
2. **Open LabVIEW examples** under `prototypes/*` or the polyglot demo under `demos/polyglot`.
3. **Generate bindings from .proto** using each language’s tooling (examples included per folder). Streaming methods use the `stream` keyword in `.proto`.

> **NI grpc‑labview** repository includes examples and notes on supported targets (Windows, Linux, NI Linux RT).

---

## References
- NI **grpc‑labview** – gRPC client/server support for LabVIEW: https://github.com/ni/grpc-labview
- NI – How to use gRPC with NI Software and Hardware: https://knowledge.ni.com/KnowledgeArticleDetails?id=kA03q000000oxQGCAY
- NI – Installing LabVIEW gRPC Library (VIPM): https://www.ni.com/docs/en-US/bundle/bts-16110/page/install-labview-grpc-library.html
- gRPC Docs – Introduction & Protocol Buffers: https://grpc.io/docs/what-is-grpc/introduction/
- Microsoft Learn – gRPC services & method types (unary/streaming): https://learn.microsoft.com/en-us/aspnet/core/grpc/services
