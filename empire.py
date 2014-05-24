import cards
import effects

#Card definition syntax:
#'Name', 'description',
#recruits cost, bricks cost, crystals cost,
#list of effects

barracks = cards.Card(
    'Barracks', '+1 recruits per turn',
    6, 0, 0,
    [effects.Economy(1, 0, 0)]
    )

militia = cards.Card(
    'Militia', '6 damage',
    2, 0, 0,
    [effects.Damage(6)]
    )

crusader = cards.Card(
    'Crusader', '12 damage',
    5, 0, 0,
    [effects.Damage(12)]
    )

sentinel = cards.Card(
    'Sentinel', '6 damage,\n+6 wall',
    5, 0, 0,
    [effects.Damage(6),
     effects.Build(0, 6)]
    )

pegasus_knight = cards.Card(
    'Pegasus Knight', '15 city damage',
    10, 0, 0,
    [effects.City_Damage(15)]
    )

paladin = cards.Card(
    'Paladin', '20 damage,\n+5 wall',
    12, 0, 0,
    [effects.Damage(20),
     effects.Build(0, 5)]
    )

swords_to_plowshares = cards.Card(
    'Swords to\nPlowshares', '+15 bricks',
    15, 0, 0,
    [effects.Resources(0, 15, 0)]
    )

archon = cards.Card(
    'Archon', '25 city damage',
    20, 0, 0,
    [effects.City_Damage(25)]
    )

mine = cards.Card(
    'Mine', '+1 bricks per turn',
    0, 6, 0,
    [effects.Economy(0, 1, 0)]
    )

house = cards.Card(
    'House', '+5 city',
    0, 2, 0,
    [effects.Build(5, 0)]
    )

wall_repairs = cards.Card(
    'Wall Repairs', '+9 wall',
    0, 3, 0,
    [effects.Build(0, 9)]
    )

fortified_wall = cards.Card(
    'Fortified Wall', '+22 wall',
    0, 10, 0,
    [effects.Build(0, 22)]
    )

church = cards.Card(
    'Church', '+15 city,\n+5 crystals',
    0, 10, 0,
    [effects.Build(15, 0),
     effects.Resources(0, 0, 5)]
    )

catapult = cards.Card(
    'Catapult', '20 damage',
    0, 12, 0,
    [effects.Damage(20)]
    )

great_wall = cards.Card(
    'Great Wall', '+50 wall',
    0, 25, 0,
    [effects.Build(0, 50)]
    )

cathedral = cards.Card(
    'Cathedral', '+30 city,\n+10 crystals',
    0, 30, 0,
    [effects.Build(30, 0),
     effects.Resources(0, 0, 10)]
    )

imperial_palace = cards.Card(
    'Imperial Palace', '+50 city',
    0, 40, 0,
    [effects.Build(50, 0)]
    )

tower = cards.Card(
    'Tower', '+1 crystals per turn',
    0, 0, 6,
    [effects.Economy(0, 0, 1)]
    )

prayer = cards.Card(
    'Prayer', '+3 crystals',
    0, 0, 1,
    [effects.Resources(0, 0, 3)]
    )

inspiration = cards.Card(
    'Inspiration', '+8 recruits',
    0, 0, 5,
    [effects.Resources(8, 0, 0)]
    )

indoctrination = cards.Card(
    'Indoctrination', 'steal 4 recruits',
    0, 0, 5,
    [effects.StealResources(4, 0, 0)]
    )

smite = cards.Card(
    'Smite', '20 damage',
    0, 0, 12,
    [effects.Damage(20)]
    )

famine = cards.Card(
    'Famine', 'opponent gets -8\nof each resources',
    0, 0, 20,
    [effects.Resources(-8, -8, -8, False)]
    )
