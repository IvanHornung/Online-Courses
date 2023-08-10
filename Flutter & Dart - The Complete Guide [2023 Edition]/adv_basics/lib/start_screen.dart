import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';


class StartScreen extends StatelessWidget {
  const StartScreen(this.startQuiz,
      {super.key}); //adding this. prefect auto sets to instance var
  // startQuiz is of type function that takes in no arguments & also doesnt return a value

  final void Function() startQuiz;

  @override
  Widget build(context) {
    return Center(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Image.asset(
            // you can wrap with Opacity widget, but not best option
            "assets/images/quiz-logo.png",
            width: 300,
            color:
                const Color.fromARGB(150, 255, 255, 255), // opacity value 150
          ),
          const SizedBox(height: 50),
          Text(
            "Learn Flutter the fun way!",
            style: GoogleFonts.lato( // 3rd party font
                color: const Color.fromARGB(255, 208, 142, 215),
                fontSize: 24,
                fontWeight: FontWeight.bold,
              ),
              textAlign: TextAlign.center,
          ),
          const SizedBox(height: 30),
          OutlinedButton.icon(
            //special constructor function for placing icon on button
            onPressed: () {
              //or simply pass `startQuiz`
              startQuiz(); // add parantheses to execute
            },
            style: OutlinedButton.styleFrom(
              foregroundColor: Colors.white,
            ),
            icon: const Icon(Icons.arrow_right_alt),
            label: const Text("Start Quiz"), //replaces child
          ),
        ],
      ),
    );
  }
}
