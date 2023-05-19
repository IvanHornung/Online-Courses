//A Bloc is a middleman between a source of data and widgets that need the data.
//Think about the "Keep me Logged In" checkbox.

import 'dart:async';
import 'validators.dart';
import 'package:rxdart/rxdart.dart';

//a mixin likes to copy&paste methods onto a base class in dart, so extend
//the most basic class (does nothing) to please dart
class Bloc extends Object with Validators {
  //we are only going to be working with String value types
  final _email =
      BehaviorSubject<String>(); //BehSub is a StreamController that captures
  //the latest item that has been added to the controller
  //-Broadcast streams allow more than one listener in the lifetime of the stream
  final _password = BehaviorSubject<String>();
  //an underscore indicates that the variable is private (for convenience for other engineers)

  // Add data to stream
  Stream<String> get email => _email.stream.transform(validateEmail);
  Stream<String> get password => _password.stream.transform(validatePassword);
  //you receive either a valid email/pass or an error msg

  Stream<bool> get submitValid => //we dont care about this v param
      Rx.combineLatest2(email, password, (e, p) => true);

  //Change data
  Function(String) get changeEmail => _email.sink.add;
  Function(String) get changePassword => _password.sink.add;

  submit() {
    final validEmail = _email.value; //BehSub.value is latest value
    final validPassword = _password.value;

    print('Email is $validEmail');
    print('Password is $validPassword');
  }

  //nothing special here, just a method to make dart happy because
  //when you create a StreamController, it auto has a sink coming with it
  //that stays open and waits forever.
  dispose() {
    _email.close();
    _password.close();
  }
}

/* 2 ways of Applying a Bloc

1. Single Global Instance
Possibly OK for small apps

2. Scoped Instances
Possibly better for large apps

*/
//1:
//final bloc = Bloc(); //one universal bloc for the entire application

/*  Important Notes on BLOCs

-We use blocs instead of StatefulWidgets to share information around our app
-We can use a bloc either as a single global instance or with a scoped instance
-Blocs use sinks and streams to work with information
-Widgets use StreamBuilders to change their contents depending on values coming
 through a stream
-The RxDart library is extremely useful in the vast majority of apps
*/
