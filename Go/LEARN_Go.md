Multiple string constants can be defined in a group

``` go
const (
    Hello = "Hello"
    World = "World"
    Greeting = Hello + " " + World
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
```

``` go
severity := pb.SeverityLevel_MEDIUM
```
