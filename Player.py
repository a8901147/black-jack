import math

from Card import Card
from Deck import Deck
from Person import Person


class Player(Person):
    def __init__(self, bet: int):
        super().__init__()
        self.__showhand = True
        self.__bet = bet

    def make_move(self, cards: list):
        for i in range(3):
            if not self.want_draw():
                return True

            self.add_cards(cards.pop(), self.__showhand)

            # there is no pts lower than 21
            if not self.get_pts:
                return False

        # should black jack and win
        return True

    def want_draw(self):
        answer = input("To player: do you want more card?\n")
        return answer == "y" or answer == "Y"

    def place_bet(self, deck: Deck):
        bet_go_to_deck = math.inf
        while bet_go_to_deck > self.__bet:
            bet_go_to_deck = int(
                input("your pocket has {} bet left, please decide how much do you want bet: ".format(self.__bet)))
        self.__bet -= bet_go_to_deck
        deck.set_bet(bet_go_to_deck)

    @property
    def get_bet(self):
        return self.__bet

    def set_bet(self, bet):
        self.__bet += bet
        # possible_pts = list(self.get_pts)
        # for val in possible_pts:
        #     if val > self.limit:
        #         self.get_pts.remove(val)
