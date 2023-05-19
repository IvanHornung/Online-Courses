
## Steps for Refactoring a StatefulWidget

1. Break the widget into two separate classes,
the `Widget` and the `Widget's State`
2. Add a `createState` method to the `Widget` class that returns an instance of `Widget State`
3. Add a build method to the `Widget State` class
4. Add instance variables to the `Widget State` class

```Dart
//Notes

void main() {
  var circleSlot = new Slot<Circle>();
  circleSlot.insert(new Circle());

}

class Circle {}
class Square {}

class Slot<T> {
  insert(T shape) {

  }
}
```