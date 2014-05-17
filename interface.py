def display(p1, p2, current_player):
    print('{:<40}{}'.format('Player 1', 'Player 2'))
    print('{:<40}{}'.format('City: ' + str(p1.city), 'City: ' + str(p2.city)))
    print('{:<40}{}'.format('Wall: ' + str(p1.wall), 'Wall: ' + str(p2.wall)))
    print('{:<40}{}'.format('Recruits: ' + str(p1.recruits) + ' (+' + str(p1.barracks) + ' per turn)',
                            'Recruits: ' + str(p2.recruits) + ' (+' + str(p2.barracks) + ' per turn)'))
    print('{:<40}{}'.format('Bricks: ' + str(p1.bricks) + ' (+' + str(p1.mines) + ' per turn)',
                            'Bricks: ' + str(p2.bricks) + ' (+' + str(p2.mines) + ' per turn)'))
    print('{:<40}{}'.format('Crystals: ' + str(p1.crystals) + ' (+' + str(p1.towers) + ' per turn)',
                            'Crystals: ' + str(p2.crystals) + ' (+' + str(p2.towers) + ' per turn)'))
    print('')

    if current_player.user == 0:
        card_counter = 1
        for card in current_player.cards.hand:
            print(card_counter, end = '. ')
            display_card(card)
            if card.playable(current_player):
                print('')
            else:
                print(' (NOT ENOUGH RESOURCES)')
            card_counter += 1
        print('')


#Prints a card's information in the format:
#Name (cost): description
def display_card(card):
    print(card.name, end = '')

    cost_strings = []
    if card.recruits_c > 0:
        recruits_string = str(card.recruits_c) + ' Recruits'
        cost_strings.append(recruits_string)
    if card.bricks_c > 0:
        bricks_string = str(card.bricks_c) + ' Bricks'
        cost_strings.append(bricks_string)
    if card.crystals_c > 0:
        crystals_string = str(card.crystals_c) + ' Crystals'
        cost_strings.append(crystals_string)

    if cost_strings == []:
        print(' (Free)', end = '')
    else:
        print(' (', end = '')
        print(cost_strings[0], end = '')
        del cost_strings[0]
        while cost_strings != []:
             print(', ' + cost_strings[0], end = '')
             del cost_strings[0]
        print(')', end = '')
    
    print(': ', end = '')
    print(card.description, end = '')

import ai

def get_input(current_player):
    if current_player.user == 0:
        while True:
            user_input = input('Choose a card to play or enter 0 to discard a card instead. ')
            if user_input in ['1', '2', '3', '4', '5', '6', '7']:
                user_input = int(user_input)
                if current_player.cards.hand[user_input - 1].playable(current_player):
                    card_index = user_input - 1
                    discard_flag = False
                    return (card_index, discard_flag)
                else:
                    print('NOT ENOUGH RESOURCES.')
            elif user_input == '0':
                user_input = input('Choose a card to discard or enter 0 to play a card instead. ')
                if user_input in ['1', '2', '3', '4', '5', '6', '7']:
                    user_input = int(user_input)
                    card_index = user_input - 1
                    discard_flag = True
                    return (card_index, discard_flag)
    if current_player.user == 1:
        return ai.random_ai(current_player)


def display_action(card_index, discard_flag, current_player):
    print('')
    if discard_flag == True:
        if current_player.user == 0:
            print('You discard:')
        else:
            print('Opponent discards:')
    else:
        if current_player.user == 0:
            print('You play:')
        else:
            print('Opponent plays:')
    display_card(current_player.cards.hand[card_index])
    print('\n')

def clear_display():
    input()
    print('\n\n\n\n\n\n\n\n')


def display_message(string):
    print(string)
