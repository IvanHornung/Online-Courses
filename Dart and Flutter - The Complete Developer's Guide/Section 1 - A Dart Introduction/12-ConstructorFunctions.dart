
void main() {
  var person = new Person('Ivan');

  person.printName();
}


class Person {
  String firstName;

  Person(firstName) {
    this.firstName = firstName;
  }
  // =
  //Person(this.firstName);


  printName() {
    print(firstName);
  }
}