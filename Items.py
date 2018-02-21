import r_world
import config


# BASE ITEM
class Item(object):
    def __init__(self, item):
        self.item = r_world.get_item_data(item)
        self.name = self.item[config.NAME]
        self.shortdesc = self.item[config.SHORTDESC]
        self.longdesc = self.item[config.LONGDESC]
        self.takeable = self.item[config.TAKEABLE]
        self.descwords = self.item[config.DESCWORDS]
        self.loottype = self.item[config.LOOTTYPE]

    def __str__(self):
        return self.name


class Weapon(Item):
    headdmg = 13000

    def __init__(self, item):
        super().__init__(item)
        self.damage = self.item[config.DAMAGE]


# LEVEL 1 DERIVED
class Consumable(Item):
    def __init__(self, item):
        super().__init__(item)
        self.amount = 1

    def use(self):
        """Use this item"""
        self.amount -= 1


if __name__ == '__main__':
    name = 'bandage'
    bn = Item(name)
    print(bn.name)