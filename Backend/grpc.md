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




testing a grpc service in command line (windows):
```

C:\Users\AdithyaES>grpcurl -plaintext dev.convin.ai:50051 list
genesis.UserFeedbackService
grpc.reflection.v1.ServerReflection
grpc.reflection.v1alpha.ServerReflection

C:\Users\AdithyaES>grpcurl -plaintext dev.convin.ai:50051 list genesis.UserFeedbackService
genesis.UserFeedbackService.GetFeedback
genesis.UserFeedbackService.GetFeedbackReport
genesis.UserFeedbackService.GetFeedbackReportStatistics
genesis.UserFeedbackService.SubmitFeedback

C:\Users\AdithyaES>grpcurl -plaintext dev.convin.ai:50051 describe genesis.UserFeedbackService.GetFeedbackReport
genesis.UserFeedbackService.GetFeedbackReport is a method:
rpc GetFeedbackReport ( .genesis.FeedbackReportRequest ) returns ( .genesis.FeedbackReportResponse );

C:\Users\AdithyaES>grpcurl -plaintext -d '{"tenantID":"sbilife","filters":"userID:convinuser;"}' dev.convin.ai:50051 genesis.UserFeedbackService.GetFeedbackReport
Error invoking method "genesis.UserFeedbackService.GetFeedbackReport": error getting request data: invalid character '\'' looking for beginning of value

C:\Users\AdithyaES>grpcurl -plaintext -d "{\"tenantID\":\"sbilife\",\"filters\":\"userID:convinuser;\"}" dev.convin.ai:50051 genesis.UserFeedbackService.GetFeedbackReport
{}

C:\Users\AdithyaES>grpcurl -plaintext -d "{\"tenantID\":\"sbilife\",\"filters\":\"userID:TestUser1;\"}" dev.convin.ai:50051 genesis.UserFeedbackService.GetFeedbackReportt
Error invoking method "genesis.UserFeedbackService.GetFeedbackReportt": service "genesis.UserFeedbackService" does not include a method named "GetFeedbackReportt"

C:\Users\AdithyaES>grpcurl -plaintext -d "{\"tenantID\":\"sbilife\",\"filters\":\"userID:TestUser1;\"}" dev.convin.ai:50051 genesis.UserFeedbackService.GetFeedbackReport
{
  "totalFeedbacks": 4,
  "results": [
    {
      "id": "sbilife:TestUser1:AI_INSIGHTS",
      "tenantID": "sbilife",
      "userID": "TestUser1",
      "featureID": "AI_INSIGHTS",
      "categories": [
        "less relevant insights",
        "minor spelling issues"
      ],
      "comment": "Hello World",
      "timestamp": "1745925623",
      "metadata": {
        "auditorname": "asdfgh",
        "conversationID": "abcdef987"
      }
    },
    {
      "id": "sbilife:TestUser1:AI_SUMMARY",
      "tenantID": "sbilife",
      "userID": "TestUser1",
      "featureID": "AI_SUMMARY",
      "feedbackType": "FeedbackType_DOWNVOTE",
      "categories": [
        "extra/unnecessary entity added"
      ],
      "timestamp": "1746132294",
      "severityLevel": "SeverityLevel_MEDIUM",
      "metadata": {
        "fields": {
          "auditorname": {
            "string_value": "yFgTEE"
          },
          "conversationID": {
            "string_value": "feDwytmK"
          }
        }
      }
    },
    {
      "id": "sbilife:TestUser1:AI_DISPOSITION",
      "tenantID": "sbilife",
      "userID": "TestUser1",
      "featureID": "AI_DISPOSITION",
      "feedbackType": "FeedbackType_DOWNVOTE",
      "categories": [
        "minor wording improvements"
      ],
      "timestamp": "1746132298",
      "severityLevel": "SeverityLevel_LOW",
      "metadata": {}
    },
    {
      "id": "sbilife:TestUser1:ENTITY_EXTRACTION",
      "tenantID": "sbilife",
      "userID": "TestUser1",
      "featureID": "ENTITY_EXTRACTION",
      "categories": [
        "less relevant insights",
        "minor spelling issues"
      ],
      "comment": "Hello World",
      "timestamp": "1745925526",
      "metadata": {
        "auditorname": "asdfgh",
        "conversationID": "abcdef987"
      }
    }
  ]
}

C:\Users\AdithyaES>

```

