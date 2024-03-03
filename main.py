
"""
Background Blackjack is a popular card game played in casinos.
The goal is to get a hand with a value as close to 21 as possible without going over.

The player is dealt (or draws) two cards and can choose to draw more or stop.

The dealer is dealt two cards as well, but only one is visible to the player.
The player wins if their hand is closer to 21 than the dealer's hand.
But if they go over 21 they automatically lose.

If the player and dealer have the same value, it's a tie.
"""
from Dealer import Dealer
from Deck import Deck
from Game import Game
from Hand import Hand
from Player import Player
from Suit import Suit
from Card import Card

"""
some question might ask:
1. pts or bargaining chip -> bargaining chip
2. how many players -> player vs dealer
3. which role: only at player side
4. dealer have to keep adding hands until over 17pts

GAME:
# player
# dealer
# bet
# deck
--------------------------------------------------------------------------------------------------------------------
CARD:
# suit 
# name

# There are 52 cards in a deck
# Each card has a suit (hearts, spades, diamonds, clubs) and there are 13 cards in each suit
# A card could be
    numbered (2-10): same pts value
    a face (jack, queen, king): 10 pts
    an ace: 1 or 11 pts, whichever is better for the player
--------------------------------------------------------------------------------------------------------------------
Suit:
------------------------------------------------------------------------------------------------------------------- 
DECK:
# init_cards:
# display_deck:
# bet:
# shuffle: 
--------------------------------------------------------------------------------------------------------------------    
PLAYER(Person)
# show_hand: 
# bet: 
--------------------------------------------------------------------------------------------------------------------  
DEALER(Person):
# show_hand: 
# bet: 
--------------------------------------------------------------------------------------------------------------------  
Person(Hand):
# make_move -> abstract class
--------------------------------------------------------------------------------------------------------------------
Hand:
# pts 
# cards
# limit = 21
"""
player = Player(100)
dealer = Dealer()
deck = Deck()
game = Game(player,dealer,deck)
game.start_game()

# player -> player allow to decide if want to draw    -> do same thing hand
# dealer -> dealer have to make a draw until over 17  -> do same thing hand