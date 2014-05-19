class Card():
    def __init__(self, name, description,
                 recruits_c, bricks_c, crystals_c,
                 effects):
        self.name = name
        self.description = description
        self.recruits_c = recruits_c
        self.bricks_c = bricks_c
        self.crystals_c = crystals_c
        self.effects = effects

### Returns True if a card is playable, False otherwise.
    def playable(self, current_player):
        if current_player.recruits < self.recruits_c:
            return False
        elif current_player.bricks < self.bricks_c:
            return False
        elif current_player.crystals < self.crystals_c:
            return False
        else:
            return True

### Applys the card's effects from first to last.
    def play(self, current_player, current_opponent):
        current_player.resources(-self.recruits_c, -self.bricks_c, -self.crystals_c)
        for effect in self.effects:
            effect.apply(current_player, current_opponent)


from random import shuffle

#PlayerCards encompasses a player's deck, hand, and discard pile.
class PlayerCards():
    def __init__(self, deck):
        self.deck = deck
        self.discard_pile = []
        self.hand = []

    def shuffle_deck(self):
        shuffle(self.deck)

    def draw_card(self):
        if self.deck != []:
            self.hand.append(self.deck[0])
            del self.deck[0]
        else:
            self.deck += self.discard_pile
            shuffle(self.deck)
            self.hand.append(self.deck[0])
            del self.deck[0]

    def draw_cards(self, number_of_cards):
        for card in range(number_of_cards):
            self.draw_card()

    def discard_card(self, card_index):
        self.discard_pile.insert(0, self.hand[card_index])
        del self.hand[card_index]

    def play_card(self, card_index, current_player, current_opponent):
        self.hand[card_index].play(current_player, current_opponent)
        self.discard_pile.insert(0, self.hand[card_index])
        del self.hand[card_index]
