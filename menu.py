from tkinter import *

class MainMenu(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title('Card Game Title')
        self.grid()

        top = self.winfo_toplevel()
        top.rowconfigure(0, weight = 1)
        top.columnconfigure(0, weight = 1)

        self.main_menu_widgets()

##-----------------------------------------------------------------------------------------
##----------------------------------------MAIN MENU----------------------------------------
##-----------------------------------------------------------------------------------------

##Creates and displays the main menu's buttons.
    def main_menu_widgets(self):
        self._menubackground = PhotoImage(file = 'menu_background.gif')
        self._menubackgroundlabel = Label(self, image = self._menubackground)
        self._menubackgroundlabel.grid(row = 0, column = 0, rowspan = 20)

        self._newgamebutton = self.menu_button('New Game', self.newgamefunction)
        self._newgamebutton.grid(row = 10, column = 0)

        self._continuegamebutton = self.menu_button('Continue Game', self.continuegamefunction)
        self._continuegamebutton.grid(row = 11, column = 0)

        self._deckmanagerbutton = self.menu_button('Deck Manager', self.deckmanagerfunction)
        self._deckmanagerbutton.grid(row = 12, column = 0)

        self._optionsbutton = self.menu_button('Options', self.optionsfunction)
        self._optionsbutton.grid(row = 13, column = 0)

        self._exitbutton = self.menu_button('Exit', self.master.destroy)
        self._exitbutton.grid(row = 14, column = 0)

##Standard button formatting for menu buttons. Returns but doesn't display a menu button.
    def menu_button(self, button_text, function):
        return Button(self, text = button_text, font = ('Nyala', 20),
                      borderwidth = 5, bg = 'tan', activebackground = 'tan',
                      command = function)

##Clears the main menu, except for its background image.
    def clear_main_menu(self):
        self._newgamebutton.grid_remove()
        self._continuegamebutton.grid_remove()
        self._deckmanagerbutton.grid_remove()
        self._optionsbutton.grid_remove()
        self._exitbutton.grid_remove()

##Response to the New Game button.
    def newgamefunction(self):
        self.clear_main_menu()
        self._menubackgroundlabel.grid_remove()
        self.initialize_battle(p1, p2)

    def continuegamefunction(self):
##        self.clear_main_menu()
        pass

    def deckmanagerfunction(self):
##        self.clear_main_menu()
        pass

    def optionsfunction(self):
##        self.clear_main_menu()
        pass

##--------------------------------------------------------------------------------------
##----------------------------------------BATTLE----------------------------------------
##--------------------------------------------------------------------------------------

##Standard label formatting for displaying in-battle player data. Returns but doesn't display
##the label object.
    def player_info_label(self, input_text, size = 15, justify_input = LEFT):
        return Label(self, text = input_text, font = ('Nyala', size),
                     bg = 'tan', relief = GROOVE, justify = justify_input)

##Standard formatting for displaying a card's button. Returns but doesn't display
##the button object.
    def card_button(self, button_text, card_index, state_input,
                    p1, p2, current_player, current_opponent):
        return Button(self, text = button_text, font = ('Nyala', 15), anchor = N,
                      borderwidth = 5, bg = 'tan', activebackground = 'tan', pady = 5,
                      relief = RIDGE, state = state_input, width = 15, height = 7,
                      command = (lambda: self.card_button_press(
                          card_index, p1, p2, current_player, current_opponent)))

##Standard formatting for displaying a card's discard button. Returns but doesn't display
##the button object.
    def discard_button(self, card_index, state_input, p1, p2, current_player, current_opponent):
        return Button(self, text = 'Discard', font = ('Nyala', 15), relief = RIDGE,
                      borderwidth = 5, bg = 'tan', activebackground = 'tan',
                      state = state_input, command = (lambda: self.discard_button_press(
                          card_index, p1, p2, current_player, current_opponent)))

##Resolves all of the actions that follow a card button being pressed.
    def card_button_press(self, card_index, p1, p2, current_player, current_opponent):
        self.update_recent_action_box(card_index, False, current_player)

        current_player.cards.play_card(card_index, current_player, current_opponent)
        current_player.cards.draw_card()

        (current_player, current_opponent) = (current_opponent, current_player)
        self.draw_battle_state(p1, p2, current_player, current_opponent)

        self.after(1500, self.new_turn, p1, p2, current_player, current_opponent)

##Resolves all of the actions that follow a discard button being pressed.
    def discard_button_press(self, card_index, p1, p2, current_player, current_opponent):
        self.update_recent_action_box(card_index, True, current_player)

        current_player.cards.discard_card(card_index)
        current_player.cards.draw_card()

        (current_player, current_opponent) = (current_opponent, current_player)
        self.draw_battle_state(p1, p2, current_player, current_opponent)

        self.after(1500, self.new_turn, p1, p2, current_player, current_opponent)

##Creates/updates and displays a card button as long as the current player is user controlled.
    def update_card_button(self, card_index, p1, p2,
                           current_player, current_opponent, disabled = False):
        card_text = current_player.cards.hand[card_index].card_string()

        if (disabled == True) or (current_player.card_is_playable(card_index) == False):
            state_input = DISABLED
        else:
            state_input = NORMAL

        self._cardbuttons[card_index] = self.card_button(card_text, card_index, state_input,
                                                         p1, p2,
                                                         current_player, current_opponent)
        self._cardbuttons[card_index].grid(row = 9, column = card_index + 2, sticky = S)

##Creates/updates and displays a card button as long as the current player is user controlled.
    def update_discard_button(self, card_index, p1, p2,
                              current_player, current_opponent, disabled = False):

        if disabled == True:
            state_input = DISABLED
        else:
            state_input = NORMAL

        self._discardbuttons[card_index] = self.discard_button(card_index, state_input, p1, p2,
                                                         current_player, current_opponent)
        self._discardbuttons[card_index].grid(row = 10, column = card_index + 2, sticky = N)



##After either player plays a card this function is called, describing the card at center-screen.
    def update_recent_action_box(self, card_index, discard_flag, current_player):
        
        if current_player.user == 0:
            action_string = 'You '
        else:
            action_string = 'Opponent '

        if discard_flag == True:
            action_string += 'discarded:\n\n'
        else:
            action_string += 'played:\n\n'

        action_string += current_player.cards.hand[card_index].card_string()

        if self._recent_action_string != None:
            self._recent_action_string.destroy()

        self._recent_action_string = self.player_info_label(action_string, 15, CENTER)
        self._recent_action_string.grid(row = 1, column = 4, rowspan = 7, columnspan = 3)


##This function is called to begin a battle.
    def initialize_battle(self, p1, p2):

        for player in (p1, p2):
            player.cards.draw_cards(7)
        current_player = p1
        current_opponent = p2

        self._battlebackground = PhotoImage(file = 'level_1.gif')
        self._battlebackgroundlabel = Label(self, image = self._battlebackground)
        self._battlebackgroundlabel.grid(row = 0, column = 0, rowspan = 11, columnspan = 11)

        for row_index in range(9):
            self.rowconfigure(row_index, weight = 1)
        self.rowconfigure(9, weight = 2)
        self.rowconfigure(10, weight = 1)

        #Initialize the list of card button and discard button widgets.
        self._cardbuttons = [None] * 7
        self._discardbuttons = [None] * 7
        self._recent_action_string = None
        self._p1citywalllabel = None
        self._p2citywalllabel = None
        self._p1resourceslabel = None
        self._p2resourceslabel = None

        self.new_turn(p1, p2, current_player, current_opponent)

##This function starts a new turn.
    def new_turn(self, p1, p2, current_player, current_opponent):
        if p1.is_alive() and p2.is_alive():
            current_player.gather()
            self.draw_battle_state(p1, p2, current_player, current_opponent)

            if current_player.user != 0:
                self.after(500, self.ai_turn, p1, p2, current_player, current_opponent)

        elif p1.is_alive():
            self._recent_action_string.configure(text = 'You win!')
            self._recent_action_string.grid()
        elif p2.is_alive():
            self._recent_action_string.configure(text = 'You lose...')
            self._recent_action_string.grid()
        else:
            self._recent_action_string.configure(text = 'Draw.')
            self._recent_action_string.grid()                

##Controls an ai opponent's turn.
    def ai_turn(self, p1, p2, current_player, current_opponent):
        (card_index, discard_flag) = ai.ai_action(current_player)

        self.update_recent_action_box(card_index, discard_flag, current_player)
        
        if discard_flag == True:
            current_player.cards.discard_card(card_index)
        else:
            current_player.cards.play_card(card_index, current_player, current_opponent)
        current_player.cards.draw_card()

        self.draw_battle_state(p1, p2, current_player, current_opponent)
        
        (current_player, current_opponent) = (current_opponent, current_player)
        self.after(1000, self.new_turn, p1, p2, current_player, current_opponent)
        

    def draw_battle_state(self, p1, p2, current_player, current_opponent):
        #Display Player 1's stats.
        self._player1label = self.player_info_label('Player 1', 40)
        self._player1label.grid(row = 2, column = 2, columnspan = 2)

        city_wall_string = 'City: ' + str(p1.city) + '\n' + 'Wall: ' + str(p1.wall)

        if self._p1citywalllabel != None:
            self._p1citywalllabel.destroy()
        self._p1citywalllabel = self.player_info_label(city_wall_string, 30)
        self._p1citywalllabel.grid(row = 3, column = 2, rowspan = 2, columnspan = 2)

        resource_string = ('Recruits: ' + str(p1.recruits) + ' (+' + str(p1.barracks) + ' per turn)'
                           + '\n' +
                           'Bricks: ' + str(p1.bricks) + ' (+' + str(p1.mines) + ' per turn)'
                           + '\n' +
                           'Crystals: ' + str(p1.crystals) + ' (+' + str(p1.towers) + ' per turn)')


        if self._p1resourceslabel != None:
            self._p1resourceslabel.destroy()
        self._p1resourceslabel = self.player_info_label(resource_string, 20)
        self._p1resourceslabel.grid(row = 5, column = 2, rowspan = 3, columnspan = 2)

        #Display Player 2's stats.
        self._player2label = self.player_info_label('Player 2', 40)
        self._player2label.grid(row = 2, column = 7, columnspan = 2)

        city_wall_string = 'City: ' + str(p2.city) + '\n' + 'Wall: ' + str(p2.wall)


        if self._p2citywalllabel != None:
            self._p2citywalllabel.destroy()
        self._p2citywalllabel = self.player_info_label(city_wall_string, 30)
        self._p2citywalllabel.grid(row = 3, column = 7, rowspan = 2, columnspan = 2)

        resource_string = ('Recruits: ' + str(p2.recruits) + ' (+' + str(p2.barracks) + ' per turn)'
                           + '\n' +
                           'Bricks: ' + str(p2.bricks) + ' (+' + str(p2.mines) + ' per turn)'
                           + '\n' +
                           'Crystals: ' + str(p2.crystals) + ' (+' + str(p2.towers) + ' per turn)')


        if self._p2resourceslabel != None:
            self._p2resourceslabel.destroy()
        self._p2resourceslabel = self.player_info_label(resource_string, 20)
        self._p2resourceslabel.grid(row = 5, column = 7, rowspan = 3, columnspan = 2)

        #Display cards.
        for card_index in range(7):
            if self._cardbuttons[card_index] != None:
                self._cardbuttons[card_index].destroy()
            if current_player.user == 0:
                self.update_card_button(card_index, p1, p2, current_player, current_opponent)
            elif current_player.user != 0 and current_opponent.user != 1:
                self.update_card_button(card_index, p1, p2,
                                        current_opponent, current_player, disabled = True)
            else:
                self.update_card_button(card_index, p1, p2,
                                        current_player, current_opponent, disabled = True)

        #Display discard buttons.
        for card_index in range(7):
            if current_player.user == 0:
                self.update_discard_button(card_index, p1, p2, current_player, current_opponent)
            else:
                self.update_discard_button(card_index, p1, p2,
                                           current_player, current_opponent, disabled = True)



##----------------------------------------Test Main----------------------------------------

import cards
import empire

p1_deck = []
p2_deck = []

for deck in (p1_deck, p2_deck):
    for card in range(4):
        deck.append(empire.barracks)
        deck.append(empire.militia)
        deck.append(empire.crusader)
        deck.append(empire.sentinel)
        deck.append(empire.pegasus_knight)
        deck.append(empire.paladin)
        deck.append(empire.swords_to_plowshares)
        deck.append(empire.mine)
        deck.append(empire.house)
        deck.append(empire.wall_repairs)
        deck.append(empire.fortified_wall)
        deck.append(empire.church)
        deck.append(empire.catapult)
        deck.append(empire.tower)
        deck.append(empire.prayer)
        deck.append(empire.inspiration)
        deck.append(empire.indoctrination)
        deck.append(empire.smite)
    for card in range(2):
        deck.append(empire.famine)
        deck.append(empire.archon)
        deck.append(empire.great_wall)
        deck.append(empire.cathedral)
        deck.append(empire.imperial_palace)

import player

p1 = player.Player(cards.PlayerCards(p1_deck))
p2 = player.Player(cards.PlayerCards(p1_deck), 1)

p1.cards.shuffle_deck()
p2.cards.shuffle_deck()

import ai

MainMenu().mainloop()
