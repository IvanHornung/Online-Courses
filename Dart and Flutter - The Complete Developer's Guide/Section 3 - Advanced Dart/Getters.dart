import 'dart:async';

void main() {
  final bloc = new Bloc();

  block.emailController.stream.listen((value) {
    print(value);
  });
//=
  bloc.emailController.listen((value) {
    print(value);
  });


  bloc.emailController.sink.add('My new email');
//=
  block.changeEmail('My new email'); //a reference to the add function
}

class Bloc {
  final emailController = StreamController<String>();

  //Add data to stream
  Function(String) get changeEmail => emailController.sink.add;
  Function(String) get changePassword => passwordController.sink.add;
  //annotate as a function that accepts a String

  //Retrieve data from stream
  Stream<String> get email /*or emailStream*/ => emailController.stream;
  Stream<String> get password => passwordController.stream;
  //annotating return type is not required, but recommended
}
