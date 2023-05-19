//This class will extend from InheritedWidget provides an instance of the Bloc
//to the widget and everything underneath it

import 'package:flutter/material.dart';
import 'bloc.dart';

class Provider extends InheritedWidget {
  final bloc = Bloc();

  //All we are doing here is taking some constructor args that would normally be provided
  //to our provider, and we are just going to forward them through to the super() class constructor
  Provider({Key key, Widget child}) : super(key: key, child: child);

  //underscore means: I dont care about his argument for this func
  bool updateShouldNotify(_) => true; //req method; only here to prevent errors

  //The of() function allows any widget at some arbitrary depth underneath (LoginScreen)
  //to magically reach back up and somehow get a handle of the InheritWidget and
  //thus the Bloc inside of it.
  static Bloc of(BuildContext context) {
    //-Context is the widget's understanding (handle/identify) of where it is located
    //in the overall Widget hierarchy.
    //-A widget can look up any number of levels above itself as far as context goes. (Linked List)
    return context.dependOnInheritedWidgetOfExactType<Provider>().bloc;
    //Deprecated use: return (context.inheritFromWidgetOfExactType(Provider) as Provider).bloc;
    //This part is saying "Hey TextField, I want you to look at your context, and
    //I want this thing to look at its parent and its parent and so on all the way
    //up the chain until it finds a widget of type Provider". This function call
    //in this line of code says "given a context, look all the way back up the tree
    //and try to find some widget of the tree that is of type Provider." This function
    //call then returns that Widget but does not necessarily know the type of Widget
    //that it returns. 'as provider' indicates that whatever you get back from the function
    //, that is going to be an instance of Provider. Then, off of that provider that
    //we retrieve, we are getting the bloc property.
  }
}
