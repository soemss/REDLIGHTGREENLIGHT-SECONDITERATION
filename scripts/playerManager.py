import sqlite3

db = sqlite3.connect("main.sqlite")
cursor = db.cursor()
cursor.execute = ('''
    CREATE TABLE IF NOT EXISTS players(
        name TEXT,
        id INTEGER, 
        score INTEGER, 
        tries INTEGER
    )
''')



class Multiplayer():
    def __init__(self):
        self.players = []

    def get_players(self):
        return self.players

    def set_players(self, player):
        self.players.append(player)
