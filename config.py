import random
import json
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
LOOTTYPE = 'loot type'
XCOORD = 'X Coordinate'
YCOORD = 'Y Coordinate'
LOCTYPE = 'location type'

DIRECTIONS = [N,NE,E,SE,S,SW,W,NW,U,D]

SCREEN_WIDTH = 80
##start_coords = [(13,5),(13,9),(13,10),(7,11),(11,11),
##                      (2,12),(3,12),(5,12),(9,12)]
starting_locations = ['Coast_13_5', 'Coast_13_9', 'Coast_13_10',
                      'Coast_7_11', 'Coast_11_11', 'Coast_2_12',
                      'Coast_3_12', 'Coast_5_12', 'Coast_9_12']
##for item in start_coords:
##    starting_locations.append('Coast_'+str(item[0])+'_'+str(item[1]))

starting_location = random.choice(starting_locations)

if __name__ == '__main__':
    print(starting_location)
