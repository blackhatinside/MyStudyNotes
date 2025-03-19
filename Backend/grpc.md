![image](https://github.com/user-attachments/assets/0c924f39-02c7-46f0-8e42-bf9ca3b82f2c)prerequisites:
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
(MyVenv) C:\AdithyaWork\CONVIN\CONVIN_PROTO\convin_proto>docker run -v C:/AdithyaWork/CONVIN/CONVIN_PROTO/convin_proto:/defs namely/protoc-all -i convin/rule_engine/v1 -f rule_engine.proto -f rule_engine_resources.proto -l python
```
after running this, 4 protos files will be generated ![Screenshot 2025-03-19 180846](https://github.com/user-attachments/assets/4d8d68a0-d762-4464-b7e1-fa15b16b0824)

replace these files in the services_proto repository ![Screenshot 2025-03-19 180929](https://github.com/user-attachments/assets/f056f1e4-ad6d-4c6a-88ba-d91625a7d207)

  

