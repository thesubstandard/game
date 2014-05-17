#The user attribute defines the controller of the player:
#   0 = human controlled

class Player():
    def __init__(self, cards, user = 0,
                 barracks = 2, mines = 2, towers = 2,
                 recruits = 4, bricks = 4, crystals = 4,
                 city = 30, wall = 10):
        self.user = user
        self.cards = cards
        self.barracks = barracks
        self.mines = mines
        self.towers = towers
        self.recruits = recruits
        self.bricks = bricks
        self.crystals = crystals
        self.city = city
        self.wall = wall

    def is_alive(self):
        if self.city > 0:
            return True
        else:
            return False

### Adjusts the player's resource collection rate.
    def economy(self, barracks, mines, towers):
        self.barracks = max(self.barracks + barracks, 1)
        self.mines = max(self.mines + mines, 1)
        self.towers = max(self.towers + towers, 1)

### Adjusts the player's resources.
    def resources(self, recruits, bricks, crystals):
        self.recruits = max(self.recruits + recruits, 0)
        self.bricks = max(self.bricks + bricks, 0)
        self.crystals = max(self.crystals + crystals, 0)

### Typically done at the start of each turn, gathers resources
    def gather(self):
        self.recruits += self.barracks
        self.bricks += self.mines
        self.crystals += self.towers

### Increases a player's city and/or wall.
    def build(self, city, wall):
        self.city += city
        self.wall = min(self.wall + wall, 100)

### Does normal damage to the player.
    def damage(self, amount):
        city_damage = max(amount - self.wall, 0)
        wall_damage = min(amount, self.wall)
        self.city -= city_damage
        self.wall -= wall_damage

### Does direct damage to the player's wall.
    def wall_damage(self, amount):
        self.wall = max(self.wall - amount, 0)

### Does direct damage to the player's city.
    def city_damage(self, amount):
        self.city = max(self.city - amount, 0)
