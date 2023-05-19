import sqlite3
from player import Player

db = sqlite3.connect("main.sqlite")
cursor = db.cursor()
cursor.execute = ('''
    CREATE TABLE IF NOT EXISTS players(
        id INTEGER PRIMARY KEY,
        name TEXT,
        score INTEGER, 
        tries INTEGER
    )
''')



class Multiplayer():
    def __init__(self,):
        self.players = []
        self.player = Player()

    def get_players(self):
        return self.players

    def set_players(self, player):
        self.players.append(player)

    def save_players(self):
        cursor = db.cursor()
        for player in self.players:
            cursor.execute("INSERT INTO players (id, name, score) VALUES (?, ?, ?)", (self.player.get_id, self.player.get_name, self.player.score))
        cursor.commit()
    
    # def load_players(self):
    #     c = db.cursor()

    #     c.execute("SELECT id, name, score FROM players")
    #     rows = c.fetchall()

    #     for row in rows:
            

