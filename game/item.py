from enum import Enum

class ItemType(Enum):
    WEAPON = "Weapon"
    HEALING = "Healing"
    MISC = "Misc"

class Item:
    def __init__(self, name=str, description=str, type=ItemType):
        self.name = name
        self.description = description
        self.type = type

    def __str__(self):
        return self.name