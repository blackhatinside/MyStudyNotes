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

