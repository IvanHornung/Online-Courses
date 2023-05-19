
void main() {
  var name = myName();
  //1 - var declares a new variable (one of many different ways you can do this in Dart)
  //2 - Variable's name is 'name'. 1&2 are variable declaration
  //3 - Runs the 'myName' function. This is variable initialization

  print('My name is $name');
  
}

String myName() {
  return 'Ivan';
}