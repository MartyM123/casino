import random
import time

def generate():
    return random.choice(['red', 'black'])

history = []
class player:
    def __init__(self):
        self.id = str(time.time())
        self.decision_function = lambda: random.choice(['red', 'black'])
        self.money=50
        self.alive=True

    def make_decision(self):
        amount=10
        return self.decision_function(), amount
    
    def on_win(self):
        print('Oh yeah!')

    def __add__(self, other):
        self.money+other
        
players = []

#create history
for i in range(10):
    history.append(dict(won=generate()))

#create players
for i in range(10):
    players.append(player())


for player in players:
    if player.alive:
        for turn in history:
            pass

print(history)