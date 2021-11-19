from enum import Enum
from abc import ABC

class CardType(Enum):
    MAJOR, MINOR = 1, 2

class Suits(Enum):
    WANDS, CUPS, PENTACLES, SWORDS = 1, 2, 3, 4

class Card(ABC):
    def __init__(self, id, arcana, name, meaning):
        self.__id = id
        self.__arcana = arcana
        self.__name = name
        self.__meaning = meaning

    def get_id(self):
        return self.__id

    def get_arcana(self):
        return self.__arcana

    def get_name(self):
        return self.__name

    def get_meaning(self):
        return self.__meaning

    def set_id(self, newId):
        self.__id = newId

    def set_arcana(self, newArcana):
        self.__arcana = newArcana

    def set_name(self, newName):
        self.__name = newName

    def set_meaning(self, newMeaning):
        self.__meaning = newMeaning


class MajorArcana(Card):
    def __init__(self, id, arcana, name, meaning):
        super().__init__(id, arcana, name, meaning)

class MinorArcana(Card):
    def __init__(self, id, arcana, number, suit, name, meaning):
        super().__init__(id, arcana, name, meaning)
        self.__number = number
        self.__suit = suit

    def set_number(self, newNumber):
        self.__arcana = newNumber

    def set_suit(self, newSuit):
        self.__suit = newSuit

    def get_number(self):
        return self.__number

    def get_suit(self):
        return self.__suit
