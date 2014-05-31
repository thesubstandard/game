#The user attribute defines the controller of the player:
#   0 = human controlled
#   1 and higher = computer controlled
#   ai 1 = random

class Player():
    def __init__(self, cards, name, user = 0,
                 barracks = 2, mines = 2, towers = 2,
                 recruits = 4, bricks = 4, crystals = 4,
                 city = 30, wall = 10):
        self.name = name
        self.user = user
        self.cards = cards
        self.buffs = []
        self.barracks = barracks
        self.mines = mines
        self.towers = towers
        self.recruits = recruits
        self.bricks = bricks
        self.crystals = crystals
        self.city = city
        self.wall = wall

    def card_is_playable(self, card_index):
        if self.cards.playable(card_index, self.recruits, self.bricks, self.crystals):
            return True
        else:
            return False

    def is_alive(self):
        if self.city > 0:
            return True
        else:
            return False

    ## Typically done at the start of each turn, gathers resources
    def gather(self):
        if self.has_buff('Blockade'):
            self.remove_buff('Blockade')
        else:
            self.recruits += self.barracks
            self.bricks += self.mines
            self.crystals += self.towers

    ##---------------------------------------------------------------##
    ##------------------------Buff Processing------------------------##
    ##---------------------------------------------------------------##
    ## Buffs are simply strings, organized in a list. When certain
    ## Effects are triggered by cards, they check the buff list and
    ## if certain buffs are present the effect might be altered.

    def has_buff(self, buff_name):
        if buff_name in self.buffs:
            return True
        else:
            return False

    def add_buff(self, buff_name):
        self.buffs.append(buff_name)

    def remove_buff(self, buff_name):
        if (buff_name in self.buffs) == True:
            self.buffs.remove(buff_name)

    ##----------------------------------------------------------------##
    ##---------------------Card Triggered Effects---------------------##
    ##----------------------------------------------------------------##

    ## Adjusts the player's resource collection rate.
    def economy(self, barracks, mines, towers):
        self.barracks = max(self.barracks + barracks, 1)
        self.mines = max(self.mines + mines, 1)
        self.towers = max(self.towers + towers, 1)

    ## Adjusts the player's resources.
    def resources(self, recruits, bricks, crystals):
        self.recruits = max(self.recruits + recruits, 0)
        self.bricks = max(self.bricks + bricks, 0)
        self.crystals = max(self.crystals + crystals, 0)

    ## Increases a player's city and/or wall.
    def build(self, city, wall):
        self.city += city
        self.wall = min(self.wall + wall, 100)

    ## Does normal damage to the player.
    def damage(self, amount):
        city_damage = max(amount - self.wall, 0)
        wall_damage = min(amount, self.wall)
        self.city = max(self.city - city_damage, 0)
        self.wall -= wall_damage

    ## Does direct damage to the player's wall.
    def wall_damage(self, amount):
        self.wall = max(self.wall - amount, 0)

    ## Does direct damage to the player's city.
    def city_damage(self, amount):
        self.city = max(self.city - amount, 0)
