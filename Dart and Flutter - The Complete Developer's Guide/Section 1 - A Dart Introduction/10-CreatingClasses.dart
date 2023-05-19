
class Person {
  String firstName;

  printName() {
    print(firstName);
    //this. is a completely valid syntax in Dart
    print(this.firstName);
  }
}