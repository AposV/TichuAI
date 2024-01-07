import random

class Rank:
    hearts = "hearts"
    clubs = "clubs"
    spades = "spades"
    diamonds = "diamonds"
    all_ranks = [hearts, clubs, spades, diamonds]


class Card:

    value = None
    rank = None
    symbol = None

    def __init__(self, value=5, rank=None):
        self.value = value
        self.rank = rank
        self.symbol = self.GetSymbol(self.value)

    def __str__(self):
        string = self.symbol

        if self.rank is not None:
            string += "_" + self.rank[0]

        return string

    @staticmethod
    def GetSymbol(value):
        if value in range(2,11):
            return str(value)
        symbols_dict = {-1: "dogs",
                        0: "phoenix",
                        1: "majong",
                        11: "J",
                        12: "Q",
                        13: "K",
                        14: "A",
                        15: "dragon"}

        if value in symbols_dict.keys():
            return symbols_dict[value]
        return "error"


class Deck:

    cards = []

    def __init__(self):
        self.GenerateDeck()
        self.Shuffle()

    def Shuffle(self):
        random.shuffle(self.cards)

    def GenerateDeck(self):
        # Generate common cards with ranks (2-A) and add them to card collection
        for rank in Rank.all_ranks:
            for value in range(2, 15):
                card = Card(value, rank)
                self.cards.append(card)

        # Add Special Cards
        majong = Card(1, None)
        dragon = Card(15, None)
        dogs = Card(-1, None)
        phoenix = Card(0, None)

        self.cards.append(majong)
        self.cards.append(dragon)
        self.cards.append(dogs)
        self.cards.append(phoenix)





