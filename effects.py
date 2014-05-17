##------Effect Superclass-----
##
##The target_self flag is a True-False attribute that determines whether the Effect instance
##affects the player that uses it.
##
##The determine_target function returns which player will be the target of the effect, based on the
##target_self flag.


class Effect():
    def __init__(self, target_self):
        self.target_self = target_self

    def determine_target(self, current_player, current_opponent):
        if self.target_self == True:
            return current_player
        else:
            return current_opponent

##------Specific Effects------


class Economy(Effect):
    def __init__(self, barracks, mines, towers, target_self = True):
        Effect.__init__(self, target_self)
        self.barracks = barracks
        self.mines = mines
        self.towers = towers

    def apply(self, current_player, current_opponent):
        target_player = self.determine_target(current_player, current_opponent)
        target_player.economy(self.barracks, self.mines, self.towers)


class Resources(Effect):
    def __init__(self, recruits, bricks, crystals, target_self = True):
        Effect.__init__(self, target_self)
        self.recruits = recruits
        self.bricks = bricks
        self.crystals = crystals

    def apply(self, current_player, current_opponent):
        target_player = self.determine_target(current_player, current_opponent)
        target_player.resources(self.recruits, self.bricks, self.crystals)


class StealResources(Effect):
    def __init__(self, recruits, bricks, crystals, target_self = False):
        Effect.__init__(self, target_self)
        self.recruits = recruits
        self.bricks = bricks
        self.crystals = crystals

    def apply(self, current_player, current_opponent):
        recruits_stolen = min(self.recruits, current_opponent.recruits)
        bricks_stolen = min(self.bricks, current_opponent.bricks)
        crystals_stolen = min(self.crystals, current_opponent.crystals)
        current_player.resources(recruits_stolen, bricks_stolen, crystals_stolen)
        current_opponent.resources(-recruits_stolen, -bricks_stolen, -crystals_stolen)


class Build(Effect):
    def __init__(self, city, wall, target_self = True):
        Effect.__init__(self, target_self)
        self.city = city
        self.wall = wall

    def apply(self, current_player, current_opponent):
        target_player = self.determine_target(current_player, current_opponent)
        target_player.build(self.city, self.wall)


class Damage(Effect):
    def __init__(self, damage, target_self = False):
        Effect.__init__(self, target_self)
        self.damage = damage

    def apply(self, current_player, current_opponent):
        target_player = self.determine_target(current_player, current_opponent)
        target_player.damage(self.damage)


class Wall_Damage(Effect):
    def __init__(self, damage, target_self = False):
        Effect.__init__(self, target_self)
        self.damage = damage

    def apply(self, current_player, current_opponent):
        target_player = self.determine_target(current_player, current_opponent)
        target_player.wall_damage(self.damage)


class City_Damage(Effect):
    def __init__(self, damage, target_self = False):
        Effect.__init__(self, target_self)
        self.damage = damage

    def apply(self, current_player, current_opponent):
        target_player = self.determine_target(current_player, current_opponent)
        target_player.city_damage(self.damage)

