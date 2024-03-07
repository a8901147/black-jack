from Card import Card


class Hand:

    def __init__(self):
        self.__pts = {0}  # set
        self.__cards = []
        self.__limit = 21

    def clear_hand(self):
        self.__pts = {0}  # set
        self.__cards = []

    def show_hands(self, visible):
        if visible:
            print("Pts:{}".format(self.__pts))
            for card in self.__cards:
                print("Suit:{}, Num:{}".format(card.get_suit.value, card.get_num))
            # player show hands
        else:
            for i in range(len(self.__cards)):
                if i == 0:
                    card = self.__cards[i]
                    print("Suit:{}, Num:{}".format(card.get_suit.value, card.get_num))
                else:
                    print("#")

    def add_cards(self, card: Card, visible: bool):
        self.__cards.append(card)
        self.__update_possible_pts(card.get_num)
        self.show_hands(visible)

    def __update_possible_pts(self, add_pts: int):
        new_possible_pts = []
        for pts in self.__pts:
            pts_map = 10 if add_pts in [11, 12, 13] else add_pts
            new_pts = pts + pts_map
            if new_pts <= self.__limit:
                new_possible_pts.append(new_pts)

        if add_pts == 1:
            for pts in self.__pts:
                new_pts = pts + 11
                if new_pts <= self.__limit:
                    new_possible_pts.append(new_pts)

        self.__pts = set(new_possible_pts)

    @property
    def get_pts(self):
        return self.__pts

    @property
    def get_cards(self):
        return self.__cards
