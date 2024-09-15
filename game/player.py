import discord
from locations.locationType import LocationType

class Player:
    def __init__(self, user:discord.User):
        self.user = user
        self.name = user.display_name
        self.hp = 100
        self.image = None
        self.location = LocationType.LOBBY

    def set_image(self, image):
        self.image = image

    def moveTo(self, location:LocationType):
        self.location = location

    def add_hp(self, amount:int):
        if self.hp + amount <= 200:
            self.hp += amount
        else:
            self.hp = 200
            
    def remove_hp(self, amount:int):
        if self.hp - amount >= 0:
            self.hp -= amount
        else:
            self.hp = 0

    def get_hp(self):
        return self.hp
    
    def get_name(self):
        return self.name
    
    def get_user(self):
        return self.user
    
    def get_location(self):
        return self.location

    def __str__(self):
        return self.name