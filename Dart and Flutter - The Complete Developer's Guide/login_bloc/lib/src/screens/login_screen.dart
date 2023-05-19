import 'package:flutter/material.dart';
import '../blocs/bloc.dart';
import '../blocs/provider.dart';

class LoginScreen extends StatelessWidget {
  Widget build(context) {
    final bloc = Provider.of(context);
    //looks at hierarchy, finds nearest instance of provider, pulls off the bloc
    //property, and returns it.

    return Container(
      margin: EdgeInsets.all(20.0),
      child: Column(
        children: <Widget>[
          emailField(bloc),
          passwordField(bloc),
          Container(margin: EdgeInsets.only(top: 25.0)),
          submitButton(bloc),
        ],
      ),
    );
  }

  Widget emailField(Bloc bloc) {
    //The StreamBuilder widget is abs core to how we update widgets inside flutter.
    return StreamBuilder(
      stream: bloc.email,
      //every time a new event comes accross ^this stream,the builder function re-runs
      //whenever the builder func gets called, it gets invoked with whatever value came
      //across the stream - which gets wrapped up in "snapshot"
      builder: (context, snapshot) {
        return TextField(
          onChanged: bloc.changeEmail,
          //same as writing (newVal){.changeEmail(newVal)}
          keyboardType: TextInputType.emailAddress,
          decoration: InputDecoration(
            hintText: 'you@example.com',
            labelText: 'Email Address',
            errorText: snapshot.error,
          ),
        );
      },
    );
  }

  Widget passwordField(Bloc bloc) {
    //Reminder: Sinks and Streams are both part of the StreamController.
    //          You add data to the StreamController using the Sink which can
    //          be listened via the Stream
    return StreamBuilder(
      stream: bloc.password, //output stream from our Bloc
      builder: (context, snapshot) {
        return TextField(
          onChanged: bloc.changePassword,
          //everytime a user types in a thing, we send that value into our password
          //stream controller's sink
          obscureText: true,
          decoration: InputDecoration(
            hintText: 'Password',
            labelText: 'Password',
            errorText: snapshot.error,
          ),
        );
      },
    );
  }

  Widget submitButton(Bloc bloc) {
    return StreamBuilder(
      stream: bloc.submitValid,
      builder: (context, snapshot) {
        return RaisedButton(
          child: Text('Login'),
          color: Colors.blue,
          onPressed: snapshot.hasData //an error is not data
              //hasData is here to grey out button before any input
              ? bloc.submit //invokes submit() in bloc class
              : null, //onPressed: null makes it appear to be disabled
        );
      },
    );
  }
}
