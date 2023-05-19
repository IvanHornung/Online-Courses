import 'dart:html';

//Game: you have 4 tries to correctly guess a word
void main() {
  final ButtonElement button = querySelector('button');
  final InputElement input = querySelector('input');

  button.onClick
      .take(4) //stream can only process count number of events
      .where((event) =>
          input.value ==
          'banana') //filters out False-valued events from the stream
      .listen((event) => print('You got it!'),
          onDone: () => print('Nope, bad guesses.'));
}
