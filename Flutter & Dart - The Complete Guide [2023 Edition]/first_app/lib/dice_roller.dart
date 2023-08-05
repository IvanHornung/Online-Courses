import 'package:flutter/material.dart';
import 'dart:math'; // for random number generation

final randomizer = Random(); //a bit more efficient


class DiceRoller extends StatefulWidget {
  const DiceRoller({super.key});

  @override
  State<DiceRoller> createState() {
    return _DiceRollerState();
  }
}

class _DiceRollerState extends State<DiceRoller> {
  var currentDiceRoll = 2;

  void rollDice() {
    setState(() { //reruns build function
      // you can use Random().nextInt() but this stores a Random object all the time
      currentDiceRoll = randomizer.nextInt(6) + 1; // 1<=6
    }); // will update it in all the places that are needed
  }

  @override
  Widget build(contenxt) {
    return Column(
      mainAxisSize: MainAxisSize.min, //take as least vertical space as possible
      children: [
        Image.asset(
          'assets/images/dice-$currentDiceRoll.png',
          width: 200,
        ),
        const SizedBox(height: 20), // widget with no content
        TextButton(
          onPressed: rollDice, //func is object, pass pointer to it
          style: TextButton.styleFrom(
              // padding: const EdgeInsets.only(
              //   top: 20,
              // ), // or you can add a sized box widget (above)
              foregroundColor: Colors.white,
              textStyle: const TextStyle(
                fontSize: 28,
              )),
          child: const Text('Roll Dice'), // keep widget arguments last
        ),
      ],
    );
  }
}
