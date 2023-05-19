
void main() {
  var person = new Person();

  person.firstName = 'Ivan';

  person.printName();
}


class Person {
  String firstName;

  printName() {
    print(firstName);
  }
}