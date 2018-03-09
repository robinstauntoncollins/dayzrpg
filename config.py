import random
NAME = 'name'
DESC = 'desc'
EXITS = 'exits'
N = 'north'
NE = 'north east'
E = 'east'
SE = 'south east'
S = 'south'
SW = 'south west'
W = 'west'
NW = 'north west'
U = 'up'
D = 'down'
GROUND = 'ground'
BUILDINGS = 'buildings'
GROUNDDESC = 'grounddesc'
SHORTDESC = 'shortdesc'
LONGDESC = 'longdesc'
TAKEABLE = 'takeable'
EDIBLE = 'edible'
DESCWORDS = 'descwords'
LOOTED = 'looted'
LOOTTYPE = 'loottype'
AMOUNT = 'amount'
XCOORD = 'X Coordinate'
YCOORD = 'Y Coordinate'
SPAWNTYPE = 'spawntype'
LOCTYPE = 'locationtype'
DAMAGE = 'damage'
MILITARY = 'military'
RESIDENTIAL = 'residential'
INDUSTRIAL = 'industrial'
MEDICAL = 'medical'
FARM = 'farm'
COAST = 'coast'
CASTLE = 'castle'
EFFECT = 'effect'




DIRECTIONS = [N,NE,E,SE,S,SW,W,NW,U,D]

SCREEN_WIDTH = 80

starting_locations = ['Coast_13_5', 'Coast_13_9', 'Coast_13_10',
                      'Coast_7_11', 'Coast_11_11', 'Coast_2_12',
                      'Coast_3_12', 'Coast_5_12', 'Coast_9_12']


starting_location = random.choice(starting_locations)

if __name__ == '__main__':
    print(starting_location)
