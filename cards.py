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
    def playable(self, recruits, bricks, crystals):
        if recruits < self.recruits_c:
            return False
        elif bricks < self.bricks_c:
            return False
        elif crystals < self.crystals_c:
            return False
        else:
            return True

### Applys the card's effects from first to last.
    def play(self, current_player, current_opponent):
        current_player.resources(-self.recruits_c, -self.bricks_c, -self.crystals_c)
        for effect in self.effects:
            effect.apply(current_player, current_opponent)

### Creates the cost portion of a card's displayed text. Used primarily in the card_string function.
    def cost_string(self):
        cost_strings = []

        if self.recruits_c > 0:
            recruits_string = str(self.recruits_c) + ' Recruits'
            cost_strings.append(recruits_string)
        if self.bricks_c > 0:
            bricks_string = str(self.bricks_c) + ' Bricks'
            cost_strings.append(bricks_string)
        if self.crystals_c > 0:
            crystals_string = str(self.crystals_c) + ' Crystals'
            cost_strings.append(crystals_string)

        if cost_strings == []:
            return ''
        else:
            output = '('
            output += cost_strings[0]
            del cost_strings[0]
            while cost_strings != []:
                output += ',\n' + cost_strings[0]
                del cost_strings[0]
            output += ')'
            return output

### Creates a card's displayed text.
    def card_string(self):
        return self.name + '\n' + self.cost_string() + '\n\n\n' + self.description


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

    def playable(self, card_index, recruits, bricks, crystals):
        if self.hand[card_index].playable(recruits, bricks, crystals):
            return True
        else:
            return False
