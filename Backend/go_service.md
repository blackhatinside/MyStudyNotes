``` bash
protoc --proto_path=protobuf "protobuf/orders.proto" --go_out=services/common/genproto/orders --go-grpc_out=services/common/genproto/orders --go_opt=paths=source_relative --go-grpc_opt=paths=source_relative
```

defer x() runs x() when the containing function ends
``` golang
logger, _ := zap.NewProduction()
defer logger.Sync()
```

In Go, constructors are usually functions named:
- `New[TypeName]`
- `[TypeName]New`
- Functions returning a pointer like `New()` or `Create()`

They're not language features but conventions.


So while both layers contain code, the actual algorithms and business logic reside in the controller, with the handler serving primarily as a translation and validation layer.
