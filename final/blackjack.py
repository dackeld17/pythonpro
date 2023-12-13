import random

suits = ['h', 'd', 'c', 's']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

class Chip(object):
    type = 'dollar'
    amount = 1
class Card(object):
    RANKS = ['A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUITS = ['c', 'd', 'h', 's']
    
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        reply = self.rank + self.suit
        return reply
class Positionable_Card(Card):
    def __str__(self):
        if self.is_face_up:
            reply = super().__str__()
        else:
            reply = "XX"
        return rep
    
    def flip(self):
        self.is_face_up = not self.is_face_up
        
    

def Deck():
    deck = [{'suit': suit, 'rank': rank} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def Positionable_Card(player, cards, hide_first_card=False):
    print(f"{player}: ", end='')
    for i, card in enumerate(cards):
        if i == 0 and hide_first_card:
            print("xx ", end='')
        else:
            print(f"{card['rank']}{card['suit']} ", end='')
    print()
def calculate(hand):
    value = 0
    num_aces = 0

    for card in hand:
        if card['rank'] in ['J', 'Q', 'K']:
            value += 10
        elif card['rank'] == 'A':
            num_aces += 1
            value += 11
        else:
            value += int(card['rank'])
           
    while num_aces > 0 and value > 21:
        value -= 10
        num_aces -= 1

    return value

def Dealer(player, hand):
    value = calculate(hand)
    print(f"{player}: {' '.join([card['rank']+card['suit'] for card in hand])} ({value})")



def BJ_Game():
    num_players = int(input("How many Players? (2-5): "))
    print()
    players = []
    for i in range(num_players):
        player_name = input(f"Enter Player name: ")
        players.append(player_name)
    deck = Deck()
    player_hands = {player: [deck.pop(), deck.pop()] for player in players}
    dealer_hand = [deck.pop(), deck.pop()]
    for player in players:
        Dealer(player, player_hands[player])
   
    Positionable_Card("dealer", dealer_hand, hide_first_card=True)
   
    for player in players:
        bet = input(f"{player}, How much will you bat($): ?")
        
   
    
    print()
    for player in players:
        sel = input(f"{player}, do you want a hit? <Y/N>")
   
if __name__ == "__main__":    
 BJ_Game()
