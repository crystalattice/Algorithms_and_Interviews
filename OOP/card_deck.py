class Card:
    """Standard playing card"""

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = 0
        self.face_card = ""
        self.available = True
        self.card_value()

    def card_value(self):
        """Determine value of non-face cards"""
        if 2 <= self.rank <= 10:
            self.value = self.rank
        else:
            self.face_card_type()

    def face_card_type(self):
        """Determine face card type and value, based on card rank"""
        if self.rank == 11:
            self.face_card = "Jack"
            self.value = 10
        elif self.rank == 12:
            self.face_card = "Queen"
            self.value = 10
        elif self.rank == 13:
            self.face_card = "King"
            self.value = 10
        elif self.rank == 1:
            self.face_card = "Ace"
            self.value = 11

    def __repr__(self):
        if not self.face_card:
            return f"{self.rank} of {self.suit}"
        else:
            return f"{self.face_card} of {self.suit}"


class Deck(Card):
    """Standard 52 card deck of cards"""

    def __init__(self, rank, suit, value=None):
        """Inherit parent class initialization and add card value"""
        super().__init__(rank, suit)
        self.value = value

    def card_value(self):
        """Call parent class' method"""
        return super().card_value()


if __name__ == "__main__":
    # Make a Deck instance that is a tuple of the card type and its value
    deck = [(Deck(rank, suit), rank) for rank in range(1, 14) for suit in ["Hearts", "Spades", "Diamonds", "Clubs"]]
    print(deck)  # Show that the Deck object is a tuple
    for card in deck:
        print(f"{card[0]}; Value = {card[1]}")  # Show the card type and its associated value
