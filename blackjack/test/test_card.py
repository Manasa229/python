import unittest

from blackjack.card import Card


class TestCard(unittest.TestCase):

    # initializing the card
    test_suit="Diamonds"
    test_value="Ace"
    test_card = Card(test_suit, test_value)

    def test_card_immutable(self):
        with self.assertRaises(AttributeError):
            print(self.test_card.__suit)
        with self.assertRaises(AttributeError):
            print(self.test_card.__value)

    def test_return_suit(self):
        self.assertEqual(self.test_card.suit(),self.test_suit)

    def test_return_value(self):
        self.assertEqual(self.test_card.value(),self.test_value)

    def test_return_representation_of_cards(self):
        self.assertEqual('{} of {}'.format(self.test_value,self.test_suit),self.test_card.__str__())

if __name__ == '__main__':
    unittest.main()