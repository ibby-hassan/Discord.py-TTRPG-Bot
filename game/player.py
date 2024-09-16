import discord
import os
from locations.locationType import LocationType
import json

class Player:
    def __init__(self, user:discord.User):
        self.user = user
        self.name = user.display_name
        self.hp = 100
        self.inventory = []
        self.location = LocationType.LOBBY

        self.save_player_to_file()
    

    """ Behaviours related to JSON memory """
    def to_json(self):
        player = {
            "user_id": self.user.id,
            "name": self.name,
            "hp": self.hp,
            "inventory": self.inventory,
            "location": self.location.name
        }
        return player
    
    def save_player_to_file(self):
            if os.path.exists('players.json'):
                with open('players.json', 'r') as f:
                    players = json.load(f)
            else:
                players = {}
            with open('players.json', 'w') as f:
                players[str(self.user.id)] = self.to_json()
                json.dump(players, f, indent=4)


    """  Gameplay related behaviours """
    def move_to(self, location:LocationType):
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