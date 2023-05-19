
//very special function that is automatically invoked by dart in execution
void main() {
  var name = myName();

  print('My name is $name');
}


//1. Type of value that will be returned
//2. name of function
//3. argument list
String myName() {
  return 'Ivan'; //function body
}