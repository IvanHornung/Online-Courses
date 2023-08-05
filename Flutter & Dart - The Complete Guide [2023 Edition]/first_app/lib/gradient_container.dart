import 'package:flutter/material.dart';
import 'package:first_app/dice_roller.dart';

// place values here for convenience. it gets too buried in widgets below
const startAlignment = Alignment.topLeft;
// is determined at compiled time unliked final. cannot do final = getAlignment()
const endAlignment = Alignment.bottomRight;

class GradientContainer extends StatelessWidget {
  final List<Color> colors;

  const GradientContainer(
      {super.key,
      required this.colors}); // synonymous with ({key}): super(key: key);

  GradientContainer.purple({super.key})  // alternate constructors
    : colors = [Colors.deepPurple, Colors.indigo];


  @override
  Widget build(context) {
    return Container(
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: colors,
          begin: startAlignment,
          end: endAlignment,
        ),
      ),
      child: const Center(
        child: DiceRoller(),
      ),
    );
  }
}
