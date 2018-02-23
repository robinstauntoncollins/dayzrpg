"""A module with functions to handle interaction with data in JSON files"""
import json
import config
import Items

PATH = r'D:\Users\RSTAUNTO\Desktop\Python\dayzrpg\resources'
WORLDPATH = PATH + '\maps\Chernarus_v5.json'
WORLDITEMSPATH = PATH + '\items'
ALLITEMS = WORLDITEMSPATH + '\worldItems.json'
WEAPONS = WORLDITEMSPATH + '\weapons.json'
FOOD = WORLDITEMSPATH + '\food.json'
MEDICAL = WORLDITEMSPATH + '\medical.json'
start = config.starting_location


def get_world_data(room_name=None, path=WORLDPATH, mode='r'):
    """A function that returns world dictionary if no name is given
    and returns specific room if name is given."""
    with open(path, mode) as file:
        world = json.load(file)
        
    if room_name is None:
        return world
    else:
        return world[room_name]


def get_item_data(item_name=None, path=ALLITEMS, mode='r'):
    """A function to retrieve data from worldItems file.
    Can be given a specific item"""
    with open(path,  mode) as file:
        world_items = json.load(file)

    if item_name is not None:
        return world_items[item_name]
    else:
        return world_items


def get_location(loc):
    """Get world location name and other info from JSON file"""
    if loc is None:
        print("r_world.get_location() Failed!")
        return
    world = get_world_data()
    for location,info in world.items():
        if loc == location:
            return location,info


def generate_items(item_type):
    """Generates a list of appropriate items based on type"""
    items = get_item_data()
    item_dict = {}
    for k,v in items.items():
        if v[config.SPAWNTYPE] == item_type:
            item_dict[k] = v

    return item_dict


def create_object(name):
    the_object = Items.Item(name)
    return the_object


def create_consumable(name, amount):
    the_object = Items.Consumable(name, amount)
    return the_object


def create_weapon(name):
    """Creates a weapon object using name and description from the json object"""
    the_object = Items.Weapon(name)
    return the_object


def populate_room(loctype):
    """Function to populate a room's ground list based on it's loot type with item objects
    when the room object is created."""

    room_items = []
    world_items = get_item_data()
    print('roadflares amount: ',world_items['roadflares'][config.AMOUNT])
    for item,info in world_items.items():
        for spawntype in info[config.SPAWNTYPE]:
            if spawntype == loctype:
                if 'weapon' in info[config.LOOTTYPE]:
                    room_items.append(create_weapon(item))
                elif 'consumable' in info[config.LOOTTYPE]:
                    print(info[config.AMOUNT])
                    room_items.append(create_consumable(item,info[config.AMOUNT]))
                else:
                    room_items.append(create_object(item))

    return room_items


def get_all_desc_words(item_list):
    """Returns a list of "description words" for each item named in item_list from world_items"""
    world_items = get_item_data()
    unique_item_list = list(set(item_list))  # make itemList unique
    desc_words = []
    for item in unique_item_list:
        desc_words.extend(world_items[item][config.DESCWORDS])
    return list(set(desc_words))


def get_all_first_desc_words(item_list):
    """Returns a list of the first "description word" in the list of
    description words for each item named in itemList."""
    world_items = get_item_data()
    unique_item_list = list(set(item_list))  # make itemList unique
    desc_words = []
    for item in unique_item_list:
        desc_words.append(world_items[item.name][config.DESCWORDS][0])
    return list(set(desc_words))


def get_first_item_matching_desc(desc, item_list):

    world_items = get_item_data()
    unique_item_list = list(set(item_list))  # make itemList unique
    for item in unique_item_list:
        if desc in world_items[item][config.DESCWORDS]:
            return item, world_items
    return None


def get_all_items_matching_desc(desc, item_list):
    world_items = get_item_data()
    unique_item_list = list(set(item_list))  # make itemList unique
    matching_items = []
    for item in unique_item_list:
        if desc in world_items[item][config.DESCWORDS]:
            matching_items.append(item)
    return matching_items,world_items


if __name__ == '__main__':
    item_list =  [Items.Item('axe'), Items.Item('baked beans')]
    matching,items = get_all_items_matching_desc('axe', item_list )

    
