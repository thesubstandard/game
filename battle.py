from tkinter import *
import ai
import copy

class Battle(Frame):
    def __init__(self, p1, p2):
        Frame.__init__(self)

        self.initialize_players(p1, p2)
        self.create_widgets()
        self.new_turn()

    def initialize_players(self, p1, p2):
        self.p1 = copy.deepcopy(p1)
        self.p2 = copy.deepcopy(p2)
        self.current_player = self.p1
        self.current_opponent = self.p2

        for player in (self.p1, self.p2):
            player.cards.draw_cards(7)
        
    def create_widgets(self):
        self.draw_background()

        self.create_player_areas()
        self.display_player_areas()

        self.create_card_buttons()
        self.display_card_buttons()
        
        self.create_start_turn_button()

    def draw_background(self):
        self._battlebackground = PhotoImage(file = 'level_1.gif')
        self._battlebackgroundlabel = Label(self, image = self._battlebackground)
        self._battlebackgroundlabel.grid(row = 0, column = 0, rowspan = 11, columnspan = 11)

    ##----------------------------------------------------------------------------------##
    ##------------------------------Battle Flow Processing------------------------------##
    ##----------------------------------------------------------------------------------##

    def new_turn(self):
        if self.p1.is_alive() and self.p2.is_alive():

            if self.p1.user == 0 and self.p2.user == 0:
                pass


            if self.current_player.user == 0:
                self.current_player.gather()
                self.update_player_areas()
                self.update_card_buttons()

            else:
                self.ai_turn()

        else:
            #end battle function
            pass

    def ai_turn(self):
        self.update_player_areas()
        self.after(1000)
        
        self.current_player.gather()
        
        self.update_player_areas()
        self.after(1000)
        
        (card_index, discard_flag) = ai.ai_action(self.current_player)
        
        self.recentactionlabel.displayrecentaction(card_index, discard_flag, self.current_player)

        if discard_flag == True:
            self.current_player.cards.discard_card(card_index)
        else:
            self.current_player.cards.play_card(card_index, self.current_player,
                                                self.current_opponent)
        self.current_player.cards.draw_card()

        self.update_player_areas()
        self.after(1000)
        
        self.end_turn()

    def end_turn(self):
        self.update_player_areas()
        
        if self.current_player.user == 0:
            self.update_card_buttons()
            self.disable_card_buttons()

        if self.current_player.user == 0 and self.current_opponent.user == 0:
            self.after(1000)
            self.hide_card_buttons()

        (self.current_player, self.current_opponent) = (self.current_opponent, self.current_player)

        if self.current_player.user == 0 and self.current_opponent.user == 0:
            self.display_start_turn_button()
        else:
            self.new_turn()


        

    ##----------------------------------------------------------------------------------##
    ##------------------------------Player Area Processing------------------------------##
    ##----------------------------------------------------------------------------------##

    ## Called at the initialization of a Battle Frame to create a player's status Labels.
    def create_player_areas(self):
        self._leftnamelabel = BattleTextLabel(self, self.p1.name, 40)
        self._leftcitywalllabel = CityWallLabel(self, self.p1)
        self._leftresourceslabel = ResourcesLabel(self, self.p1)

        self._rightnamelabel = BattleTextLabel(self, self.p2.name, 40)
        self._rightcitywalllabel = CityWallLabel(self, self.p2)
        self._rightresourceslabel = ResourcesLabel(self, self.p2)

        self.recentactionlabel = RecentActionLabel(self)
        self.recentactionlabel.grid(row = 1, column = 4, rowspan = 7, columnspan = 3)

    ## Updates both player's status Labels.
    def update_player_areas(self):
        self._leftcitywalllabel.updatestring()
        self._leftresourceslabel.updatestring()

        self._rightcitywalllabel.updatestring()
        self._rightresourceslabel.updatestring()

        self.update()

    ## Displays both player's status Labels.
    def display_player_areas(self):
        left_column = 2
        right_column = 7
        standard_width = 2
        
        self._leftnamelabel.grid(row = 2, column = left_column, columnspan = standard_width)
        self._leftcitywalllabel.grid(row = 3, rowspan = 2,
                                     column = left_column, columnspan = standard_width)
        self._leftresourceslabel.grid(row = 5, rowspan = 3,
                                      column = left_column, columnspan = standard_width)

        self._rightnamelabel.grid(row = 2, column = right_column, columnspan = standard_width)
        self._rightcitywalllabel.grid(row = 3, rowspan = 2,
                                     column = right_column, columnspan = standard_width)
        self._rightresourceslabel.grid(row = 5, rowspan = 3,
                                      column = right_column, columnspan = standard_width)
        

    ##-----------------------------------------------------------------------------##
    ##------------------------------Button Processing------------------------------##
    ##-----------------------------------------------------------------------------##

    ## Called at the initialization of a Battle Frame to create the Card Buttons.
    def create_card_buttons(self):
        self._playercards = []
        self._discardbuttons = []
        for card in range(7):
            self._playercards.append(CardButton(self, '', card))
            self._discardbuttons.append(DiscardButton(self, card))


    ## Updates and then displays the Card Buttons.
    def display_card_buttons(self):
        for card in range(7):
            self.update_card_buttons()
            self._playercards[card].grid(row = 9, column = card + 2, sticky = S)
            self._discardbuttons[card].grid(row = 10, column = card + 2, sticky = N)

    ## Removes the Card Buttons, saving their grid options.    
    def hide_card_buttons(self):
        self.disable_card_buttons()
        for card in self._playercards:
            card.configure(text = '')
        self.update()

    ## Disables the Card Buttons so they are visible but not pressable.
    def disable_card_buttons(self):
        for card in self._playercards:
            card.configure(state = DISABLED)
        for button in self._discardbuttons:
            button.configure(state = DISABLED)
        self.update()

    ## Updates the text, state, and command function of the Card Buttons.
    def update_card_buttons(self):
        for card in self._playercards:
            card.updatecard(self, self.current_player, self.current_opponent)
        for button in self._discardbuttons:
            button.updatecommand(self, self.current_player)
        self.update()

    def create_start_turn_button(self):
        self._startturnbutton = StartTurnButton(self, self.current_player)

    def display_start_turn_button(self):
        self._startturnbutton.update_text(self.current_player)
        self._startturnbutton.grid(row = 9, column = 0, columnspan = 11)

    def hide_start_turn_button(self):
        self._startturnbutton.grid_remove()
        

##-------------------------------------------------------------------------------------##
##------------------------------Standard Label Formatting------------------------------##
##-------------------------------------------------------------------------------------##

## Most general standard formatting for in-battle text.
class BattleTextLabel(Label):
    def __init__(self, parent, input_text, size = 15, justify_input = LEFT):
        Label.__init__(self, parent, text = input_text, font = ('Nyala', size),
                       bg = 'tan', relief = GROOVE, justify = justify_input)
        

## Specific type of BattleTextLabel used to display a player's current city and wall levels.
class CityWallLabel(BattleTextLabel):
    def __init__(self, parent, player):
        self.owner = player
        BattleTextLabel.__init__(self, parent, self.citywallstring(), 30)

    def citywallstring(self):
        return 'City: ' + str(self.owner.city) + '\n' + 'Wall: ' + str(self.owner.wall)

    def updatestring(self):
        self.configure(text = self.citywallstring())

## Specific type of BattleTextLabel used to display a player's current resource levels.
class ResourcesLabel(BattleTextLabel):
    def __init__(self, parent, player):
        self.owner = player
        BattleTextLabel.__init__(self, parent, self.resourcesstring(), 20)

    def resourcesstring(self):
        return ('Recruits: ' + str(self.owner.recruits) + ' (+' + str(self.owner.barracks) +
                ' per turn)' + '\n' +
                'Bricks: ' + str(self.owner.bricks) + ' (+' + str(self.owner.mines) +
                ' per turn)' + '\n' +
                'Crystals: ' + str(self.owner.crystals) + ' (+' + str(self.owner.towers) +
                ' per turn)')

    def updatestring(self):
        self.configure(text = self.resourcesstring())

## Specific type of BattleTextLabel used to display the most recent action a player has taken.
class RecentActionLabel(BattleTextLabel):
    def __init__(self, parent):
        BattleTextLabel.__init__(self, parent, '', 15, CENTER)
        self.configure(width = 18, height = 10)

    def displayrecentaction(self, card_index, discard_flag, current_player):
        action_string = str(current_player.name)

        if discard_flag == True:
            action_string += ' discarded:\n\n'
        else:
            action_string += ' played:\n\n'

        action_string += current_player.cards.hand[card_index].card_string()

        self.configure(text = action_string)

##--------------------------------------------------------------------------------------##
##------------------------------Standard Button Formatting------------------------------##
##--------------------------------------------------------------------------------------##

class DiscardButton(Button):
    def __init__(self, parent, card_index):
        Button.__init__(self, parent, text = 'Discard', font = ('Nyala', 15), relief = RIDGE,
                        borderwidth = 5, bg = 'tan', activebackground = 'tan', command = None)
        self.card_index = card_index

    def updatecommand(self, parent, current_player):
        new_command = lambda: self.command(parent, current_player)
        self.configure(command = new_command, state = NORMAL)

    def command(self, parent, current_player):
        parent.recentactionlabel.displayrecentaction(self.card_index, True, current_player)

        current_player.cards.discard_card(self.card_index)
        current_player.cards.draw_card()

        parent.end_turn()

class CardButton(Button):
    def __init__(self, parent, input_text, card_index):
        Button.__init__(self, parent, text = input_text, font = ('Nyala', 15), anchor = N,
                        borderwidth = 5, relief = RIDGE, bg = 'tan', activebackground = 'tan',
                        pady = 5, width = 15, height = 7, command = None)
        self.card_index = card_index

    def updatecard(self, parent, current_player, current_opponent):
        new_text = current_player.cards.hand[self.card_index].card_string()

        if current_player.card_is_playable(self.card_index):
            new_state = NORMAL
        else:
            new_state = DISABLED

        new_command = lambda: self.command(parent, current_player, current_opponent)

        self.configure(text = new_text, state = new_state, command = new_command)

    def command(self, parent, current_player, current_opponent):
        parent.recentactionlabel.displayrecentaction(self.card_index, False, current_player)

        current_player.cards.play_card(self.card_index, current_player, current_opponent)
        current_player.cards.draw_card()

        parent.end_turn()

class StartTurnButton(Button):
    def __init__(self, parent, current_player):
        Button.__init__(self, parent, font = ('Nyala', 15), borderwidth = 5, relief = RIDGE,
                        bg = 'tan', activebackground = 'tan', command = lambda: self.command(parent))
        init_text = "Start "
        init_text += current_player.name
        init_text += "'s turn."
        self.configure(text = init_text)

    def update_text(self, current_player):
        init_text = "Start "
        init_text += current_player.name
        init_text += "'s turn."
        self.configure(text = init_text)

    def command(self, parent):
        parent.new_turn()
        parent.hide_start_turn_button()
        parent.display_card_buttons()

        
























        
