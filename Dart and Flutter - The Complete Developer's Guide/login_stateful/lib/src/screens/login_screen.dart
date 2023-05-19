import 'package:flutter/material.dart';
import '../mixins/validation_mixin.dart';

class LoginScreen extends StatefulWidget {
  createState() {
    return LoginScreenState();
  }
}

class LoginScreenState extends State<LoginScreen> with ValidationMixin {
  final formKey =
      GlobalKey<FormState>(); //conformed to expect a FormState instance
  String email = '';
  String password = '';

  Widget build(context) {
    return Container(
      margin: EdgeInsets.all(20.0),
      child: Form(
        key: formKey, //assigns GlobalKey
        child: Column(
          children: <Widget>[
            emailField(),
            passwordField(),
            Container(margin: EdgeInsets.only(top: 25.0)),
            submitButton(),
          ],
        ),
      ),
    );
  }

  //helper methods to prevent congestion and make code easier to read
  Widget emailField() {
    return TextFormField(
      keyboardType:
          TextInputType.emailAddress, //adjusts keyboard for email input
      decoration: InputDecoration(
        labelText: 'Email Address',
        hintText: 'you@example.com',
      ),
      validator: validateEmail, //passing reference of the function
      onSaved: (String value) {
        email = value;
      },
    );
  }

  Widget passwordField() {
    return TextFormField(
      //putting spacing works here, but is not as maintainable code
      //What happens if we swap the spots of the 2 text fields??
      obscureText: true, //obscures text
      decoration: InputDecoration(
        labelText: 'Password',
        hintText: 'Password',
      ),
      validator: validatePassword,
      onSaved: (String value) {
        password = value;
      },
    );
  }

  Widget submitButton() {
    //has a little bit of shadowing underneath it
    return RaisedButton(
      color: Colors.blue,
      child: Text('Submit!'),
      onPressed: () {
        if (formKey.currentState.validate()) {
          formKey.currentState.save();
          //take *both* email and password and post them to some API
          print('Time to post $email and $password to my API');
        }
      },
    );
  }
}

//Notes:
//To reference a widget that has been rendered to the screen of the device,
//you create a GlobalKey.

//The global key gives us the ability to reference a very specific widget
//and reference properties and call methods that are associated with that widget.
