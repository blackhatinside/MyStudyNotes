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





``` bash
(MyVenv) C:\AdithyaWork\CONVIN\CONVIN_PROTO\convin_proto>pip install grpcio grpcio-tools
(MyVenv) C:\AdithyaWork\CONVIN\CONVIN_PROTO\convin_proto>python -m grpc_tools.protoc -I . --python_out=convin/rule_engine/ --grpc_python_out=convin/rule_engine/ convin/rule_engine/v1/rule_engine_resources.proto
```
after running this, 2 protos files will be generated ![Screenshot 2025-03-19 164529](https://github.com/user-attachments/assets/0a7d40e1-d0e4-45e3-a42a-83b07f98d578)

replace these files in the services_proto repository ![Uploading Screenshot 2025-03-19 164807.png…]()

