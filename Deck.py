from Card import Card
from Suit import Suit
import random


class Deck:

    def __init__(self):
        self.__cards = Deck.init_cards()
        self.__bet = 0

    @staticmethod
    def init_cards():
        cards = []
        for num in range(1,14):
            for s in Suit:
                cards.append(Card(num,s))
        return cards

    def clear_deck(self):
        self.__cards = Deck.init_cards()
        self.__bet = 0

    def shuffle(self):
        random.shuffle(self.__cards)

    def remove_card(self):
        card = self.__cards.pop()
        return card

    @property
    def get_cards(self):
        return self.__cards

    @property
    def get_bet(self):
        return self.__bet

    def set_bet(self, bet):
        self.__bet = bet
