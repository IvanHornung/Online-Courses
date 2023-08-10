import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

import 'package:adv_basics/answer_button.dart';
import 'package:adv_basics/data/questions.dart';

class QuestionsScreen extends StatefulWidget {
  const QuestionsScreen({super.key, required this.onSelectAnswer});

  final void Function(String answer) onSelectAnswer;

  @override
  State<QuestionsScreen> createState() {
    return _QuestionsScreenState();
  }
}

class _QuestionsScreenState extends State<QuestionsScreen> {
  var currentQuestionIndex = 0;

  void answerQuestion(String selectedAnswer) {
    widget.onSelectAnswer(selectedAnswer); //widget property is within State class and lets us access Stateful class
    setState(() {
      currentQuestionIndex++;
    });
  }

  @override
  Widget build(context) {
    final currentQuestion = questions[currentQuestionIndex];

    return SizedBox(
      // alternative to Center and MainAxisSize.min
      width: double
          .infinity, // use as much width as you can. handles horizontal position
      child: Container(
        margin: const EdgeInsets.all(
            40), // adds spacing in all directions around button
        child: Column(
          mainAxisAlignment:
              MainAxisAlignment.center, //handles verticle position
          crossAxisAlignment: CrossAxisAlignment
              .stretch, //horizontal component of buttons themselves
          children: [
            Text(
              currentQuestion.text,
              style: GoogleFonts.lato( // 3rd party font
                color: const Color.fromARGB(255, 208, 142, 215),
                fontSize: 24,
                fontWeight: FontWeight.bold,
              ),
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: 30),
            //... is spread operation
            ...currentQuestion.getShuffledAnswers().map((answer) {
              //input implied from list elements
              return AnswerButton(
                answerText: answer,
                onTap: () { // cant pass pointer because we have an argument this time; use anonymous func
                  answerQuestion(answer); //only executed when anonymous func is triggered
                },
              );
            }),
          ],
        ),
      ),
    );
  }
}
