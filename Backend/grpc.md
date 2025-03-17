prerequisites:
  - protoc-30.1-win64.zip (add to PATH - C:\Users\AdithyaES\Downloads\protoc-30.1-win64\bin)
  - 
``` bash
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
```

#*#*#
``` bash
(MyVenv) C:\AdithyaWork\grpc_projects\grpc_demo>python server.py


(MyVenv) C:\AdithyaWork\grpc_projects\grpc_demo>go mod tidy
(MyVenv) C:\AdithyaWork\grpc_projects\grpc_demo>go run client.go
```
