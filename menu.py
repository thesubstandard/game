from tkinter import *
import battle

class MainMenu(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.draw_background()
        self.create_main_menu_buttons()
        self.display_main_menu_buttons()

    def draw_background(self):
        self._menubackground = PhotoImage(file = 'menu_background.gif')
        self._menubackgroundlabel = Label(self, image = self._menubackground)
        self._menubackgroundlabel.grid(row = 0, column = 0, rowspan = 20)

    def create_main_menu_buttons(self):
        self._campaignbutton = MenuButton(self, 'Campaign', self.campaignfunction)
        self._practicebutton = MenuButton(self, 'Practice', self.practicefunction)
        self._deckmanagerbutton = MenuButton(self, 'Deck Manager', self.deckmanagerfunction)
        self._optionsbutton = MenuButton(self, 'Options', self.optionsfunction)
        self._exitbutton = MenuButton(self, 'Exit', self.exitfunction)

    def display_main_menu_buttons(self):
        self._campaignbutton.grid(row = 10, column= 0)
        self._practicebutton.grid(row = 11, column = 0)
        self._deckmanagerbutton.grid(row = 12, column = 0)
        self._optionsbutton.grid(row = 13, column = 0)
        self._exitbutton.grid(row = 14, column = 0)

    def hide_main_menu(self):
        self.grid_remove()


    def campaignfunction(self):
        self.hide_main_menu()

    def practicefunction(self):
        self.hide_main_menu()
        self._practicebattle = battle.Battle(p1, p2)
        self._practicebattle.grid()

    def deckmanagerfunction(self):
        pass

    def optionsfunction(self):
        pass

    def exitfunction(self):
        self.master.destroy()
        

class MenuButton(Button):
    def __init__(self, parent, input_text, function):
        Button.__init__(self, parent, text = input_text, command = function,
                        font = ('Nyala', 20), borderwidth = 5, bg = 'tan',
                        activebackground = 'tan')

##----------------------------------------Test Players----------------------------------------

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

p1 = player.Player(cards.PlayerCards(p1_deck), 'Player 1')
p2 = player.Player(cards.PlayerCards(p1_deck), 'Player 2', 1)

p1.cards.shuffle_deck()
p2.cards.shuffle_deck()
