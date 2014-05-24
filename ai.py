from copy import copy
import random

def ai_action(current_player):
    if current_player.user == 1:
        return random_ai(current_player)


#Player user type 1:
#This ai randomly chooses between playable cards, if any, or randomly discards
#if there are none.
def random_ai(current_player):
    
    playable_cards = list(range(7))
    for card in range(7):
        if current_player.card_is_playable(card) == False:
            playable_cards.remove(card)

    if playable_cards == []:
        card_index = random.randint(0, 6)
        discard_flag = True
    else:
        card_index = random.choice(playable_cards)
        discard_flag = False
    return (card_index, discard_flag)
