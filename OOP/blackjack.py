import random

from card_deck import Card, Deck


def create_deck():
    """Create a deck of 52 cards for play"""
    deck = [(Deck(rank, suit), rank) for rank in range(1, 14) for suit in ["Hearts", "Spades", "Diamonds", "Clubs"]]

    return deck


def deal_cards(deck):
    """Deal two cards to a player"""
    players_hand = []
    random.shuffle(deck)
    for i in range(2):
        new_card = deck.pop()
        players_hand.append(new_card)

    return players_hand


def hand_total(players_hand):
    """Calculate the value of a player's hand"""
    total = 0
    for card in players_hand:
        if 11 <= card[1] <= 13:  # Face cards
            total += 10
        elif card[1] == 1:  # Ace card
            if total >= 11:
                total += 1
            else:
                total += 11
        else:
            total += card[1]

    return total


def hit(players_hand, deck):
    """Player wants another card"""
    new_card = deck.pop()
    players_hand.append(new_card)

    return players_hand


def score(players_hand, dealers_hand):
    """Determine the value of a hand"""
    player = hand_total(players_hand)
    dealer = hand_total(dealers_hand)
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


if __name__ == "__main__":
    player_hand = []
    dealer_hand = []

    game_deck = create_deck()
    player_cards = deal_cards(game_deck)
    dealer_cards = deal_cards(game_deck)

    for card in player_cards:
        player_hand.append(card[0])
    print(f"You have the following cards: {player_hand} for a score of {hand_total(player_cards)}")

    for card in dealer_cards:
        dealer_hand.append(card[0])
    print(f"The dealer has the following cards: {dealer_hand} for a score of {hand_total(dealer_cards)}")

    score(player_cards, dealer_cards)
    # print(player_cards)
    # print(hand_total(player_cards))
    # print(hit(player_cards, game_deck))
    # print(hand_total(player_cards))
