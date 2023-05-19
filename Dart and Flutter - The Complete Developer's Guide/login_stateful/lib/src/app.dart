import 'package:flutter/material.dart';
import 'screens/login_screen.dart';

class App extends StatelessWidget {
  Widget build(context) {
    //when we create a MaterialApp, it gives us a couple of very
    //default elements that we would expect to have in any mobile app ie navigation.
    return MaterialApp(
      title: 'Log Me In!',
      home: Scaffold(
        //we want the default component to show up
        //to the screen to be Scaffold that had a body
        //of some amount of text
        body: LoginScreen(),
      ),
    );
  }
}
