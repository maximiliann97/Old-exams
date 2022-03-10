from enum import Enum
from collections import defaultdict


class StorageType(Enum):
    Freezer = 0
    Cold = 1
    Standard = 2


class StorageUnit(Enum):
    kg = 0
    liter = 1
    cans = 2
    pieces = 3


class InventoryItem:
    def __init__(self, name, storage=StorageType.Standard, unit=StorageUnit.pieces):
        self.name = name
        self.storage = storage
        self.unit = unit

    def __lt__(self, other):
        return self.name < other.name

    def __repr__(self):
        return f'InventoryItem({str(self.name)}, {self.storage}, {self.unit})'

    def __hash__(self):
        return hash(self.name)


class Inventory:
    def __init__(self, name):
        self.name = name
        self.inventory = defaultdict(int)

    def add(self, item, amount):
        if amount < 0:
            raise ValueError

        self.inventory[item] += amount

    def remove(self, item, amount):

        if item not in self.inventory:
            raise KeyError

        if amount < 0:
            raise ValueError

        if self.inventory[item] - amount < 0:
            raise ValueError

        self.inventory[item] -= amount

    def __repr__(self):
        return f'{self.name}: {self.inventory.items()}'


inv = Inventory('Kitchen')
print(inv)
beans = InventoryItem('Beans', unit=StorageUnit.cans)
rice = InventoryItem('Rice', unit=StorageUnit.kg)
egg = InventoryItem('Egg', storage=StorageType.Cold)

inv.add(beans, 4)
inv.add(rice, 0.5)
inv.add(rice, 0.5)
inv.add(egg, 6)
print(inv)
inv.remove(beans, 2)
inv.remove(egg, 1)
print(inv)

try:
    inv.remove(InventoryItem('Concrete'), 1)
    print(f'Wow, did we store concrete in the {inv.name}!')
except KeyError:
    print(f'No concrete in the {inv.name}!')
try:
    inv.remove(egg, 10)
    print(f'Wow, plenty of eggs in the {inv.name}!')
except ValueError:
    print(f'Not enough eggs in the {inv.name}!')