import packages.Tichu.Cards as Cards
from packages.GameManagement.CardDealer import Dealer
from packages.GameManagement.Player import Player

dealer = Dealer()

pl1 = Player()
pl2 = Player()
pl3 = Player()
pl4 = Player()

players = [pl1, pl2, pl3, pl4]

dealer.DealCardsToPlayers(players)

for p in players:
    p.PrintHand()