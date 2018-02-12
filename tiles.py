import Item
from Weapons import Axe


class MapTile:
    '''Abstract Base Class For World locations'''
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()


class StartingCoast(MapTile):
    def intro_text(self):
        return '''You find yourself on the coast of an unknown land.
                  You see a road running along the coast to your left and right
                  and, behind it, a line of hills densly covered in pine forest.\n
                  To the north, along the coast road, about 300 meters away,
                  you see a collection of houses.'''

    def modify_player(self, player):
        # Area has no effect on Player
        pass


class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x,y)

    def intro_text(self):
        return '''Loot Room Text.'''

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, x,y, enemy):
        self.enemy = enemy
        super().__init__(x,y)

    def intro_text(self):
        return '''Loot Room Text.'''

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining".format(self.enemy.damage, the_player.hp))
            
