import interface

def initialize_battle(p1, p2):

    for player in (p1, p2):
        player.cards.draw_cards(7)

    battle_loop(p1, p2)

def battle_loop(p1, p2):

    current_player = p1
    current_opponent = p2

    while p1.is_alive() and p2.is_alive():
        current_player.gather()
        interface.display(p1, p2, current_player)
        (card_index, discard_flag) = interface.get_input(current_player)
        if discard_flag == False:
            interface.display_action(card_index, discard_flag, current_player)
            current_player.cards.play_card(card_index, current_player, current_opponent)
        else:
            interface.display_action(card_index, discard_flag, current_player)
            current_player.cards.discard_card(card_index)
        current_player.cards.draw_card()
            
        (current_player, current_opponent) = (current_opponent, current_player)
        interface.clear_display()

    if p1.is_alive():
        interface.display_message('You win!')
        interface.clear_display()
    elif p2.is_alive():
        interface.display_message('You lose...')
        interface.clear_display()
    else:
        interface.display_message('You both lose.')
        interface.clear_display()
