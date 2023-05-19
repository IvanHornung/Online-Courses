void main() {
  var deck = new Deck();
  //deck.shuffle();
  
  print(deck);
  deck.removeCard('Diamonds', 'Ace');
  print(deck);
}


class Deck {
  List<Card> cards = [];

  Deck() {
    var ranks = ['Ace', 'Two', 'Three', 'Four', 'Five'];
    var suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades'];
    for(var suit in suits) {
      for(var rank in ranks) {
        var card = new Card(
          suit: suit,
          rank: rank
          );
        cards.add(card);
      } 
    }
  }

  toString() {
    return cards.toString();
  }

  //List<E> shuffle() is a built-in method
  shuffle() {
    cards.shuffle();
  }

  cardsWithSuit(String suit) {
    return cards.where((card) => card.suit == suit );
  }

  deal(int handSize) {
    var hand = cards.sublist(0, handSize);
    cards = cards.sublist(handSize);
    return hand;
  }

  removeCard(String suit, String rank) {
    cards.removeWhere((card) => (card.suit == suit) && 
      (card.rank == rank));
  }
}

class Card {
  String suit;
  String rank;


  Card({this.suit, this.rank});

  toString() {
    return '$rank of $suit';
  }
}