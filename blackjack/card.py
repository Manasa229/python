# Blackjack
import random
from typing import List


class Card:

    def __init__(self, suit: str, value: str):
        self.__suit = suit
        self.__value = value

    def suit(self) -> str:
        return self.__suit

    def value(self) -> str:
        return self.__value

    def __str__(self) -> str:
        return "{} of {}".format(self.__value, self.__suit)







