/*Characteristics of a Cake Factory

-The factory receives an 'order', does some processing on it, then spits
  out a cake on the other end
-The factory isn't built when the order is made. The factory is made ahead of time
-The factory spends a lot of time sitting around waiting for an order to come in
-Someone has to stand around waiting for an order to come in. This is the 
  'entry point' into the factory.
-After a cake is made, someone has to come pick it up
*/

import 'dart:async';

class Cake {}

class Order {
  String type;
  Order(this.type);
}

void main() {
  final controller = new StreamController(); //consists of sink -> stream

  final order = new Order('banana');

  //3. BAKER: The StreamTranformer. Looks at incoming values, does processing on them,
  //          then adds them back into the stream.
  final baker = new StreamTransformer.fromHandlers(
    handleData: (cakeType, sink) {
      //this is a separate sink from #1. If you call sink.add with this one, it adds adds a value
      // where the /'s are. If you call sink.add with the transformer, it doesnt start the entire
      //process over again, it just adds a new value that continues on from the .transform step forward.
      if (cakeType == 'chocolate') {
        sink.add(new Cake());
      } else {
        sink.addError('I cant bake that type!');
      }
    },
  );

  //1. ORDER TAKER: The StreamController's sink.add function. Adds a new value
  //             to be processed by the stream (factory where processing is done)
  controller.sink.add(order);

//"order inspector": takes order and pulls out relevent information
  controller.stream
      //2. ORDER INSPECTOR: The 'map' function of the stream. Looks at each value that
      //                 comes in to the stream, does some processing on it, then returns it.
      .map((order) => //Arrow function has implicit return keyword
          order.type) //Purpose: just extract the type of cake we wanted.
      .transform(baker)
      /////////////////
      .listen((cake) => print('Heres your $cake'),
          onError: (err) => print(err));
  //4. PICKUP OFFICE: The 'listen' function. First argument gets called with values
  //   that made it through the stream without errors. 'onError' called with any errors
  //   produced during the stream processing.
}
