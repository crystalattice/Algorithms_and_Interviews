import random


class Card:
    """Standard playing card"""
    def __init__(self, value, rank, suit):
        self.value = value
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return self.rank + " of " + self.suit


class Deck:
    """Standard 52 card deck of cards"""
    def __init__(self):