``` bash
protoc --proto_path=protobuf "protobuf/orders.proto" --go_out=services/common/genproto/orders --go-grpc_out=services/common/genproto/orders --go_opt=paths=source_relative --go-grpc_opt=paths=source_relative
```

defer x() runs x() when the containing function ends
``` golang
logger, _ := zap.NewProduction()
defer logger.Sync()
```
