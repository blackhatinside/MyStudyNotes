# Remote Procedure Calls
  - distributed, client-server based applications
  - called procedure may not be in same address space as calling procedure
  - types:
    - callback RPC: enables p2p between processes
    - broadcast RPC: client's request is sent to all servers in the network (helps reduce load)
    - sends requests from client to server in batches
    - 




// Contains Production-related information  
message Production {
  string id = 1;
  string title = 2;
  ProductionFormat format = 3;
  repeated ProductionScript scripts = 4;
  ProductionSchedule schedule = 5;
  // ... more fields
}

service ProductionService {
  // returns Production by ID
  rpc GetProduction (GetProductionRequest) returns (GetProductionResponse);
}

message GetProductionRequest {
  string production_id = 1;
}

message GetProductionResponse {
  Production production = 1;
}





FieldMask fieldMask = FieldMask.newBuilder()
    .addPaths("title")
    .addPaths("schedule.last_updated_by.email")
    .build();

GetProductionRequest request = GetProductionRequest.newBuilder()
    .setProductionId(LA_CASA_DE_PAPEL_PRODUCTION_ID)
    .setFieldMask(fieldMask)
    .build();
