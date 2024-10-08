import discord

class Player:
    def __init__(self, name:str, user:discord.User):
        self.name = name
        self.user = user
        self.hp = 100

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

    def __str__(self):
        return self.name