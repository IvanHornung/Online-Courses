

import 'dart:async';

main() {
  print('About to fetch data...');
  
  //v1
  get('http://lasljdas')
    .then((result) {
      print(result);
    });
  
  //v2
  var result = await get('http://ospodkas');
  print(result);
}

Future<String> get(String url) {
  return new Future.delayed(new Duration(seconds: 3), () {
    return 'Got the data!';
  });
}