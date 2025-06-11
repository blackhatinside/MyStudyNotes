Multiple string constants can be defined in a group

``` go
const (
    Hello = "Hello"
    World = "World"
    Greeting = Hello + " " + World
)
```

``` go
type word string // user defined datatype 'word' of type string
const (
    Hello word = "Hello"
    World word = "World"
    Greeting word = Hello + " " + World
)
```

``` go
const Hello = "Hello"
const World = "World"
```


Protobuf enums are implemented as constants with integer values in Go.

``` proto
enum SeverityLevel {
    SeverityLevel_NO_ISSUES = 0;
    SeverityLevel_LOW = 1;
    SeverityLevel_MEDIUM = 2;
    SeverityLevel_HIGH = 3;
}

severity := pb.SeverityLevel_MEDIUM
```

Using String() on a Protocol Buffer enum in Go will return the name of the enum value as a string. 

``` go
enum Feature {
    Feature_UNSPECIFIED = 0;
    Feature_AI_DISPOSITION = 1;
    Feature_AI_SUMMARY = 2;
    Feature_AI_INSIGHTS = 3;
    Feature_AI_SENTIMENT_ANALYSIS = 4;
    Feature_SCORE_SENSE = 5;
    Feature_ENTITY_EXTRACTION = 6;
}

feedback := model.UserFeedback{
    TenantID:     req.TenantID,
    UserID:       req.UserID,
    Feature:      model.FeatureChoices(req.Feature.String()),
    FeedbackType: convertFeedbackType(req.FeedbackType),
    Categories:   req.Categories,
    Comment:      req.Comment,
    Timestamp:    time.Now().Unix(),
}
```

In Go, only identifiers starting with an uppercase letter are exported and accessible from other packages.



```
import (
    "reflect"
)

reflect.TypeOf(whatever_variable_name)
```


To get a proto file(go get bitbucket.org/convin/convin_proto/src/master/convin/bark/v1/bark_resources.proto)  (update it locally, by pulling from convin_proto)
``` bash
go get bitbucket.org/convin/convin_proto
go mod tidy
go mod vendor
```

- Make changes to convin_proto repo file
- go-genproto repo file will be generated automatically


``` bash
docker run --rm -v $(pwd):/defs namely/protoc-all -f bark_resources.proto -l go
protoc --go_out=. --go_opt=paths=source_relative bark_resources.proto
```
