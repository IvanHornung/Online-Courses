
void main() {
  var name = myName();

  print('My name is $name.length');
  //would print "My name is Ivan.length"
  print('My name is ${name.length}');
  //fixes this.
  print('My name is ${name}');
  //its not a bad idea to put curley braces whenever possible
}

String myName() {
  return 'Ivan';
}