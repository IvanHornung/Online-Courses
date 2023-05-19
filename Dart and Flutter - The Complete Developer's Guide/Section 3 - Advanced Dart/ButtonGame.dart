import 'dart:html';

//Game where you lose when you stop pressing the button for 1 second
void main() {
  final ButtonElement button = querySelector('button');

  button.onClick
      .timeout(
        new Duration(seconds: 1),
        onTimeout: (sink) => sink.addError('You lost!'),
      )
      .listen((event) {}, onError: (err) => print(err));
}

/* Soooo... Why Steams?

-A lot of Dart + Flutter libraries return streams that you and I can work with
-We can compose streams out of easily reusable functions
-Can be really easy to read streams and understand how they modify data
-Streams are all about time series of data - far easier to do some time-related stuff with streams
*/
