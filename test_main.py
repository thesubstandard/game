import cards
import empire

p1_deck = []
p2_deck = []

for deck in (p1_deck, p2_deck):
    for card in range(4):
        deck.append(empire.militia)
        deck.append(empire.crusader)
        deck.append(empire.sentinel)
        deck.append(empire.pegasus_knight)
        deck.append(empire.house)
        deck.append(empire.wall_repairs)
        deck.append(empire.fortified_wall)
        deck.append(empire.church)
        deck.append(empire.indoctrination)
        deck.append(empire.smite)

import player

p1 = player.Player(cards.PlayerCards(p1_deck))
p2 = player.Player(cards.PlayerCards(p1_deck), 1)

p1.cards.shuffle_deck()
p2.cards.shuffle_deck()

import battle

battle.initialize_battle(p1, p2)
