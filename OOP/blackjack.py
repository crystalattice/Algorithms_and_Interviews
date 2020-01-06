import random

from card_deck import Deck


class Game:
    """Generate a deck for a particular game"""

    def __init__(self):
        self.deck = [(Deck(rank, suit), rank) for rank in range(1, 14)
                     for suit in ["Hearts", "Spades", "Diamonds", "Clubs"]]
        self.players_hand = self.initial_deal()
        self.dealers_hand = self.initial_deal()

    def initial_deal(self):
        """Deal two cards to a player"""
        hand = []
        random.shuffle(self.deck)
        for i in range(2):
            new_card = self.deck.pop()
            hand.append(new_card)

        return hand

    @staticmethod
    def hand_total(hand):
        """Calculate the value of a player's hand"""
        total = 0
        for current_card in hand:
            if 11 <= current_card[1] <= 13:  # Face cards
                total += 10
            elif current_card[1] == 1:  # Ace card
                if total >= 11:
                    total += 1
                else:
                    total += 11
            else:
                total += current_card[1]

        return total

    def hit(self, hand):
        """Player wants another card"""
        new_card = self.deck.pop()
        hand.append(new_card)

        return hand

    def blackjack(self):
        """Determine if initial deal is a winner"""
        player = self.hand_total(self.players_hand)
        dealer = self.hand_total(self.dealers_hand)

        if player == 21 and dealer < 21:
            print(f"You have blackjack. You win!")
        elif dealer == 21 and player < 21:
            print(f"The dealer has blackjack. You lose!")
            exit()

    def score(self):
        """Determine the value of a hand"""
        player = self.hand_total(self.players_hand)
        dealer = self.hand_total(self.dealers_hand)

        if player == dealer:
            print(f"You both have the same score. You push.")
        elif player > 21 > dealer:
            print(f"You busted with a score of {player}.")
        elif dealer > 21 > player:
            print(f"The dealer busted with a score of {dealer}.")
        elif player == 21 and dealer < 21:
            print(f"You have blackjack. You win!")
        elif dealer == 21 and player < 21:
            print(f"The dealer has blackjack. You lose!")
        elif dealer < player < 21:
            print(f"You beat the dealer with a score of {player}.")
        elif player < dealer < 21:
            print(f"The dealer beat you with a score of {dealer}.")

    @staticmethod
    def display_hand(cards):
        """Show the cards in the hand"""
        for card in cards:
            print(card[0])


if __name__ == "__main__":
    game = Game()
    players_hand = game.players_hand
    dealers_hand = game.dealers_hand

    print(f"Your cards:")
    game.display_hand(players_hand)
    print(f"Your current score is {game.hand_total(players_hand)}")

    print(f"\nDealer's cards:")
    game.display_hand(dealers_hand)
    print(f"Dealer's current score is {game.hand_total(dealers_hand)}")

    game.blackjack()

    choice = input("\nDo you want to [h]it or [s]tand? ").lower()
    if choice == "h" or choice == "hit":
        game.hit(players_hand)
        print(f"Your cards:")
        game.display_hand(players_hand)
        while game.hand_total(dealers_hand) < 17:
            game.hit(dealers_hand)
            print(f"\n Dealer's cards:")
            game.display_hand(dealers_hand)
        game.score()
    elif choice == "s" or choice == "stand":
        while game.hand_total(dealers_hand) < 17:
            game.hit(dealers_hand)
            print(f"Dealer's cards:")
            game.display_hand(dealers_hand)
        game.score()
