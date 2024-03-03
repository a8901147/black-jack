import enum


class Card:
    def __init__(self, num: int, suit: enum):
        self.__suit = suit
        self.__num = num
        #self.__pts = self.pts_map(num)
    """
    @staticmethod
    def pts_map(num):
        if num in [11, 12, 13]:
            return [10]
        elif num == 1:
            return [1,11]
        else:
            return [num]
    """
    @property
    def get_suit(self):
        return self.__suit

    @property
    def get_num(self):
        return self.__num

    """
    @property
    def get_pts(self):
        return self.__pts
    """
