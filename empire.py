import cards
import effects

#Card definition syntax:
#'Name', 'description',
#recruits cost, bricks cost, crystals cost,
#tuple of effects

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
    'Sentinel', '6 damage and +6 wall',
    5, 0, 0,
    [effects.Damage(6),
     effects.Build(0, 6)]
    )

pegasus_knight = cards.Card(
    'Pegasus Knight', '15 city damage',
    10, 0, 0,
    [effects.City_Damage(15)]
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
    'Church', '+15 city, +5 crystals',
    0, 10, 0,
    [effects.Build(15, 0),
     effects.Resources(0, 0, 5)]
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
