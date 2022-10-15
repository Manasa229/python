import random
from typing import List

from blackjack.card import Card
from blackjack.deck import Deck


class Blackjack:
    card_value_pair = {"Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8,
                       "Nine": 9, "Ten": 10, "Jack": 10,
                       "Queen": 10, "King": 10}

    # Creates a blackjack with a new Deck.
    def __init__(self):
        self.new_deck=Deck()
        self.current_deck = self.new_deck.deck
        self.discard_pile = []
        self.current_hand = []
        self.previous_current_hand=[]

    # Computes the score of a hand.
    # For examples of hands and scores as a number.
    # 2,5 -> 7
    # 3, 10 -> 13
    # 5, King -> 15
    # 10, Ace -> 21
    # 10, 8, 4 -> Bust so return -1
    # 9, Jack, Ace -> 20
    # If the Hand is a bust return -1 (because it always loses)
    def _get_score(self, hand: List[Card]) -> int:
        score = 0
        ace_flag = 0
        for card in hand:
            if "Ace" == card.value():
                ace_flag = 1
                score += 11
            else:
                score += self.card_value_pair[card.value()]
        if ace_flag and score > 21:
            score -= 10
        if score > 21:
            return -1
        return score

    # Prints the current hand and score.
    # E.g. would print out (Ace of Clubs, Jack of Spades, 21)
    # E.g. (Jack of Clubs, 5 of Diamonds, 8 of Hearts, "Bust!")
    def _print_current_hand(self) -> None:
        current_hand_str = ""
        for card in self.current_hand:
            if card.value() == 'Ace' or card.value() == 'Jack' or card.value() == 'Queen' or card.value() == 'King':
                value = card.value()
            else:
                value = self.card_value_pair[card.value()]

            current_hand_str += ('{} of {}, '.format(value, card.suit()))
        score = self._get_score(self.current_hand)
        if score == -1:
            current_hand_str += "Bust!"
        else:
            current_hand_str += (str(score))
        print(current_hand_str)

    # The previous hand is discarded and shuffled back into the deck.
    # Should remove the top 2 cards from the current deck and
    # Set those 2 cards as the "current hand".
    # It should also print the current hand and score of that hand.
    # If less than 2 cards are in the deck,
    # then print an error instructing the client to shuffle the deck.
    def deal_new_hand(self) -> None:
        self.discard_pile=self.previous_current_hand

        if len(self.current_deck) < 2:
            raise Exception("Shuffle the deck")
        self.current_hand = self.current_deck[:2]
        self.previous_current_hand=self.current_hand
        for card in self.previous_current_hand:
            self.current_deck.remove(card)
        self._print_current_hand()

    # Deals one more card to the current hand and prints the hand and score.
    # If no cards remain in the deck, print an error.
    def hit(self) -> None:
        if (len(self.current_deck)) < 0:
            raise Exception("cannot call hit on an empty hand")

        self.previous_current_hand = self.current_deck[:1]
        for card in self.previous_current_hand:
            self.current_deck.remove(card)
            self.current_hand.append(card)
        self._print_current_hand()

    # Reshuffles all cards in the "current hand" and "discard pile"
    # and shuffles everything back into the Deck.
    def reshuffle(self) -> None:
        Blackjack()



blackjack = Blackjack()

blackjack.deal_new_hand()
blackjack.deal_new_hand()
blackjack.hit()
blackjack.hit()
blackjack.hit()
blackjack.hit()
blackjack.reshuffle()
