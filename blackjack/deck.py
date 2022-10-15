import random

from blackjack.card import Card


class Deck:
    deck = []

    def __init__(self):
        SUITS = ["Diamonds", "Spades", "Hearts", "Clubs"]
        VALUES = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen",
                  "King"]
        self.deck=[]
        for suit in SUITS:
            for value in VALUES:
                new_card = Card(suit, value)
                self.add_card(new_card)
        self.shuffle()

    # Returns the number of Cards in the Deck
    def size(self) -> int:
        return len(self.deck)

    # Shuffles the deck of cards. This means randomzing the order of the cards in the Deck.
    def shuffle(self) -> None:
        random.shuffle(self.deck)

    # Returns the top Card in the deck, but does not modify the deck.
    def peek(self) -> Card:
        return self.deck[-1]

    # Removes and returns the top card in the deck. The card should no longer be in the Deck.
    def draw(self) -> Card:
        top_card = self.deck[-1]
        self.deck.remove(self.deck[-1])
        return top_card

    # Adds the input card to the deck.
    # If the deck has more than 52 cards, do not add the card and raise an exception.
    def add_card(self, card: Card) -> None:
        if len(self.deck) > 52:
            raise Exception('Not enough space on dec')
        self.deck.append(card)

    # Calling this function should print all the cards in the deck in their current order.
    def print_deck(self) -> None:
        if len(self.deck) > 0:
            for card in self.deck:
                print(card)

    # Resets the deck to it's original state with all 52 cards.
    # Also shuffle the deck.
    def reset(self) -> None:
        reset_deck = Deck()
        self.shuffle()
