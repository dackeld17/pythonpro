class Card:
    """ A playing card. """
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["c","d","h","s"]
    
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        reply = self.rank + self.suit
        return reply
        
class Hand:
    """A hand of playing cards."""
    def __init__(self):
        self.cards = []
        
    def __str__(self):
        if self.cards:
            reply = ""
            for card in self.cards:
                reply += str(card) + " "
        else:
            reply = "<empty>"
        return reply
    def clear(self):
        self.cards = []
        
    def add(self,card):
        self.cards.append(card)
    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)
class Deck(Hand):
    """ A deck of playing cards. """
    
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Out of cards!")
                    
if __name__ == "__main__":
        print("Created a new deck.")
        deck1 = Deck()
        print("Deck:\n",deck1)
        
        deck1.populate()
        print("\nPopulated the deck.\n",deck1)
        
        deck1.shuffle()
        print("\nShuffled the deck.\n",deck1)
        
        my_hand = Hand()
        your_hand = Hand()
        hands = [my_hand,your_hand]
        deck1.deal(hands, per_hand = 5)
        print("\nDealt 5 cards to my hand and your hand.")
        print("\nMy hand:\n",my_hand)
        print("\nYour hand:\n",your_hand)
        print("\nDeck:\n",deck1)
        deck1.clear()
        print("\nCleared the deck.\n",deck1)
