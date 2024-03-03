from Card import Card
from Person import Person


class Dealer(Person):
    def __init__(self):
        super().__init__()
        self.__showhand = False

    def make_move(self, cards:list):
        for i in range(3):
            if max(self.get_pts)>17:
                return True

            self.add_cards(cards.pop(),False)
            if not self.get_pts:
                return False

        # should black jack and win
        return True
