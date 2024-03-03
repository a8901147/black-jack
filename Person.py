from abc import ABC, abstractmethod

from Card import Card
from Hand import Hand


class Person(Hand, ABC):

    @abstractmethod
    def make_move(self, cards:list):
        pass

