# codable-generator-python
coable generator python3

```json
{"name":"bens","color":"#fff","price":1300000,"size":{"width":2.8,"height":1.7,"length":4.9}}
```

```swift
struct Size: Codable{

    var width : Float = 0.0
    var height : Float = 0.0
    var length : Float = 0.0

}
struct Outer: Codable{

    var name : String = ""
    var color : String = ""
    var price : Int = 0
    var size : Size

}
```

## use
1. download py to your mac
2. open term
3. input python3 codable-genertor.py -f src2.json -o Outer -t struct

## params

    -f pathname
    -o className
    -t struct/class
    -c copy to clipboard
    -np not print the text in console

## LICENSE
BSD v3
