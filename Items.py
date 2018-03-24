import r_world
import config


# BASE ITEM
class Item(object):
    def __init__(self, item):
        self.item = r_world.get_item_data(item)
        self.name = self.item[config.NAME]
        self.raw = self.name.strip().lower()
        self.amount = self.item[config.AMOUNT]
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
    def __init__(self, item, amount = 1):
        super().__init__(item)
        self.amount = amount
        self.effect = self.item[config.EFFECT]
        self.usable = True

    def __str__(self):
        return "{0}, {1} - {2}".format(self.name, self.amount, self.shortdesc)

    def use(self):
        """Use this item"""
        if self.usable and self.amount >= 1:
            self.amount -= 1
            return self.effect, self.amount
        else:
            self.usable = False
            print("None left")
            return None


if __name__ == '__main__':
    flrs = Consumable('roadflares',10)
    bnd = Consumable('bandage', 1)
    print(bnd)
    bnd.use()
    print(bnd)
    bnd.use()
