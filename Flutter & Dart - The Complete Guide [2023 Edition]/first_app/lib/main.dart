import 'package:flutter/material.dart';
import 'package:first_app/gradient_container.dart';

void main() {
  runApp(
    const MaterialApp(
      home: Scaffold(
        body: GradientContainer(
          colors: [
            Color.fromARGB(255, 68, 11, 165),
            Color.fromARGB(255, 132, 103, 182),
          ],
        ),
      ),
    ),
  );
}
