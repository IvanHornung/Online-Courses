import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class QuestionsSummary extends StatelessWidget {
  const QuestionsSummary(this.summaryDate, {super.key});

  final List<Map<String, Object>> summaryDate;

  Color determineIndexColor(String correctAnswer, String givenAnswer) {
    return (correctAnswer == givenAnswer)
        ? const Color.fromARGB(255, 129, 204, 235)
        : const Color.fromARGB(255, 241, 109, 213);
  }

  // BETTER SOLUTION: make question number its own widget, and make each individual row its own widget
  // My solution below. 

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 350,
      child: SingleChildScrollView(
        child: Column(
          children: summaryDate.map(
            (data) {
              return Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Container(
                    width: 30,
                    height: 30,
                    // padding: const EdgeInsets.all(10),
                    // alignment: Alignment.bottomLeft,
                    alignment: Alignment.center,
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(100),
                      // shape: BoxShape.circle,
                      color: determineIndexColor(
                        data['correct_answer'] as String,
                        data['user_answer'] as String,
                      ),
                    ),
                    child: Text(
                      ((data['question_index'] as int) + 1).toString(),
                      style: GoogleFonts.lato(
                        fontWeight: FontWeight.bold,
                        fontSize: 15,
                      ),
                    ),
                  ), // `as` used for typecasting
                  const SizedBox(
                    width: 15,
                  ),
                  Expanded(
                    //column takes an inf amount of width
                    child: Column(
                      children: [
                        Container(
                          alignment: Alignment.centerLeft,
                          child: Text(
                            data['question'] as String,
                            style: GoogleFonts.lato(
                              fontWeight: FontWeight.bold,
                              color: const Color.fromARGB(229, 255, 255, 255),
                              fontSize: 16,
                            ),
                            textAlign: TextAlign.left,
                          ),
                        ),
                        const SizedBox(
                          height: 3,
                        ),
                        Container(
                          alignment: Alignment.centerLeft,
                          child: Text(
                            data['user_answer'] as String,
                            style: GoogleFonts.lato(
                              fontWeight: FontWeight.w500,
                              color: const Color.fromARGB(117, 255, 255, 255),
                              fontSize: 15,
                            ),
                          ),
                        ),
                        Container(
                          alignment: Alignment.centerLeft,
                          child: Text(
                            data['correct_answer'] as String,
                            style: GoogleFonts.lato(
                              fontWeight: FontWeight.w500,
                              color: const Color.fromARGB(255, 111, 180, 201),
                              fontSize: 15,
                            ),
                          ),
                        ),
                        const SizedBox(
                          height: 2,
                        ),
                      ],
                    ),
                  ),
                ],
              );
            },
          ).toList(),
        ),
      ),
    );
  }
}
