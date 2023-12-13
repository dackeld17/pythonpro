import random

suits = ['h', 'd', 'c', 's']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def clear_deck():
    deck = [{'suit': suit, 'rank': rank} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
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

def print_cards(player, cards, hide_first_card=False):
    print(f"{player}: ", end='')
    for i, card in enumerate(cards):
        if i == 0 and hide_first_card:
            print("xx ", end='')
        else:
            print(f"{card['rank']}{card['suit']} ", end='')
    print()

def print_hand(player, hand):
    value = calculate_hand_value(hand)
    print(f"{player}: {' '.join([card['rank']+card['suit'] for card in hand])} ({value})")


def blackjack_game():
    num_players = int(input("How many Players? (2-5): "))
    print()
    players = []
    for i in range(num_players):
        player_name = input(f"Enter Player name: ")
        players.append(player_name)
    deck = clear_deck()
    player_hands = {player: [deck.pop(), deck.pop()] for player in players}
    dealer_hand = [deck.pop(), deck.pop()]
   
    print()
    for player in players:
        print_hand(player, player_hands[player])
   
    print_cards("dealer", dealer_hand, hide_first_card=True)
   
if __name__ == "__main__":    
 blackjack_game()
