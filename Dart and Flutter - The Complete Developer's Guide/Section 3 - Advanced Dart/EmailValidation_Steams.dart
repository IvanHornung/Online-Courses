import 'dart:html';
import 'dart:async';

void main() {
  final InputElement input = querySelector('input');
  final DivElement div =n querySelector('div');

  final validator = new StreamTransformer.fromHandlers(
    handleData: (inputValue, sink) {
      if (inputValue.contains('@')) {
        sink.add(inputValue);
      } else {
        sink.addError('Enter a valid email');
      }
    },
  );

  input.onInput
      .map((dynamic event) => event.target.value)
      .transform(validator)
      //.transform(validateNotGmailAddress) you can stack as many validators as you want here
      .listen((inputValue) => div.innerHtml = '',
          onError: (err) => div.innerHtml = err);
}

//Input data stream from a widget -> BLOC -> Output datastream to a widget