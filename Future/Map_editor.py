import json
# CONSTANTS
NAME = 'name'
DESC = 'desc'
EXITS = 'exits'
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
LOCTYPE = 'locationtype'
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

WORLDPATH = r'D:\Users\RSTAUNTO\Desktop\Python\dayzrpg\Future\Chernarus_v4.json'
TESTPATH = r'D:\Users\RSTAUNTO\Desktop\Python\dayzrpg\Future\test_fix.json'
location_types = ['large city', 'city', 'large town',
               'town', 'small town', 'village',
               'small vilage', 'airfield', 'military base']
DIRECTIONS = [N, NE, E, SE, S, SW, W, NW, U, D]

#SCHEMAs
#Locations
Chernarus = {
    "Map Location": { # Program usable name, not for display to players
        NAME:'', # Name for display to players
        DESC:'', #Description of Location, uesd in intro_text()
        LOCTYPE:'', #Type of location eg. airfield, 
        EXITS: {
            N:'',
            NE:'',
            E:'',
            SE:'',
            S:'',
            SW:'',
            W:'',
            NW:''
        },
        GROUND : 'ground',
        BUILDINGS : [],
        GROUNDDESC : 'grounddesc',
        SHORTDESC : 'shortdesc',
        LONGDESC : 'longdesc',
        TAKEABLE : 'takeable',
        EDIBLE : 'edible',
        DESCWORDS : 'descwords',
        LOOTED : False,
        LOOTTYPE : 'loot type',
        XCOORD : 'X Coordinate',
        YCOORD : 'Y Coordinate'
        }
    }

town_template = [DESC, N, NE, E, SE, S, SW, W, NW, XCOORD, YCOORD]

building_template = []

container_template = []


def write_map(template):
    graph = {}
    while True:
        new_location = str(input("Enter new location(type 'quit' to exit loop): "))
        if new_location == 'quit':
            break

        
        graph[new_location] = {}
        for k in template:
            text = str(input("Enter {}:".format(k)))
            if text == '':
                pass
            else:
                graph[new_location][k] = text

        print(graph)
    print("loop has broken now!")
    graph_json = json.dumps(graph)
    with open('Chernarus.json', 'w') as file:
        file.write(graph_json)
        
    return graph


def add_ground_items(world,item):
    for k,v in world.items():
        v[GROUND].append(item)

def add_locations(world, template):
    world = json.loads(world)
    for item in world:
        for k,v in item.items():
            print(k,v)
    while True:
        new_location = str(input("Enter new location(type 'quit' to exit loop): "))
        if new_location == 'quit':
            break
        
        for k in template:
            text = str(input("Enter {}:".format(k)))
            if text == '':
                pass
            else:
                graph[new_location][k] = text
    graph_json = json.dumps(graph)
    with open('Chernarus.json', 'a') as file:
        file.write(graph_json)
        
    return graph


def load(PATH):
    """Loads a world from a given filepath and parses it into a dictionary"""
    with open(PATH,'r') as file:
        world = json.load(file)
    return world


def delete_key(location,key):
    """Deletes an entry from a location"""
    del location[key]


def add_key(location,key):
    """Adds a key to a single location"""
    location[key] = []


def add_sub_dict(location, dict_name, dict_itself):
    """Adds a sub dictionary to a single location"""
    location[dict_name] = dict_itself


def get_exits(location):
    """Given a particular location, returns exits"""
    exits = {}
    for k, v in location.items():
        if k in DIRECTIONS:
            exits[k] = v
    return exits


def write_new_world(world):
    """Converts world dict to json and writes it to a new file"""
    world_json = json.dumps(world, indent=4, sort_keys=False)
    filename = str(input("Enter the file name: "))
    filename = filename+'.json'
    with open(filename, 'w') as new:
        new.write(world_json)
    return


def edit(world):
    for k,v in world.items():
        v[config.GROUND] = []

    return world


def add_names(world):
    for k,v in world.items():
        v[NAME] = k
    return world


def fix_names(world):
    for k,v in world.items():
        if k.startswith('Coast'):
            v[NAME] = 'Coast'
    return world

def add_loctype(world):
    
    military = 'military'
    residential = 'residential'
    industrial = 'industrial'
    medical = 'medical'
    farm = 'farm'
    coast = 'coast'
    castle = 'castle'
    loctype = None
    for location,info in world.items():
        print("Current Location: {}".format(location))
        loctype = int(input("Enter 0)Military, 1)Residential, 2)Farm 3)Medical 4)Industrial, 5)Coast, 6)Castle : "))
        if loctype == 0:
            info[LOCTYPE] = military
        elif loctype == 1:
            info[LOCTYPE] = residential
        elif loctype == 2:
            info[LOCTYPE] = farm
        elif loctype == 3:
            info[LOCTYPE] = medical
        elif loctype == 4:
            info[LOCTYPE] = industrial
        elif loctype == 5:
            info[LOCTYPE] = coast
        elif loctype == 6:
            info[LOCTYPE] = castle
        else:
            print("unknown type")
            info[LOCTYPE] = None

    return world

if __name__ == '__main__':
    fix_world = load(WORLDPATH)
    new_world = add_loctype(fix_world)
    #print(new_world)
    write_new_world(new_world)

