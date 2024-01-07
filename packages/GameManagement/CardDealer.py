import packages.Tichu.Cards as Cards

class Dealer:

    deck = None

    def __init__(self):
        self.deck = Cards.Deck()

    def DealCardsToPlayers(self, players):

        cards = self.deck.cards
        cards_per_player = len(cards)/4

        cardSplits = []
        for i in range(4):
            startIdx = int(cards_per_player*i)
            endIdx = int(startIdx + cards_per_player)
            split = cards[startIdx:endIdx]
            cardSplits.append(split)

        if len(players) == 4:
            for index, player in enumerate(players):
                player.cardsInHand = cardSplits[index]



