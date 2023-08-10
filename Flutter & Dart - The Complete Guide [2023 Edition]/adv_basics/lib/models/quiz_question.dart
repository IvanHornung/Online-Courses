class QuizQuestion {
  const QuizQuestion(this.text, this.answers);

  final String text;
  final List<String> answers;

  List<String> getShuffledAnswers() {
    //chaining: calling a method as a result of calling another one
    final shuffledList = List.of(answers); //final. we can do this bc does not overwrite the list as a whole
    shuffledList.shuffle(); //creates a new list from another list. basically copies
    return shuffledList;
  }
}