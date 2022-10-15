import random
import unittest
from unittest.mock import MagicMock

from blackjack.card import Card
from blackjack.deck import Deck


class TestDeck(unittest.TestCase):
    test_deck = Deck()

    def test_deck_size(self):
        self.assertEqual(self.test_deck.size(),52)

    def test_reset_deck(self):
        self.test_deck.reset()
        self.assertEqual(self.test_deck.size(),52)

if __name__ == '__main__':
    unittest.main()
