class Player:

    cardsInHand = None

    def __init__(self):
        self.cardsInHand = []

    def PrintHand(self):
        print([str(c) for c in self.cardsInHand])


