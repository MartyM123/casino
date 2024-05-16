import random
import time
import matplotlib.pyplot as plt

random.seed(1)
def generate():
    return random.choice(['red', 'black'])

class player:
    def __init__(self):
        self.id = str(random.randint(1, 10**6))
        self.decision_function = lambda: random.choice(['red', 'black'])
        self.money=50
        self.alive=True

    def make_decision(self):
        amount=10
        return self.decision_function(), amount
    
    def on_win(self, *args, **kwargs):
        pass
        
    def on_lose(self, *args, **kwargs):
        pass

    def __add__(self, other):
        self.money=self.money+other
    
    def __sub__(self, other):
        self.money=self.money-other

    def __str__(self):
        return str(f'model id: {self.id}, money: {self.money}')

def create_history(players, n_turns):
    # set parameters
    history = []

    #create history with known victory colors
    for i in range(n_turns):
        history.append(dict(won=generate()))


    for player in players:
        if player.alive:
            for turn in range(len(history)):
                tip, amount = player.make_decision()
                amount=min([player.money, amount]) #to be sure that player won't bet more than he has
                if tip == history[turn]['won']:
                    player+amount
                    player.on_win()
                    history[turn][str(player.id)]=dict(tip=tip, amount=amount, balance=player.money)
                else:
                    player-amount
                    player.on_lose()
                    history[turn][str(player.id)]=dict(tip=tip, amount=amount, balance=player.money)
    return history

if True == False:
    n_turns=100 #number of turn of rulet
    n_players=2 #number of players

    players = []
    #create players
    for i in range(n_players):
        players.append(player())

    history=create_history(players, n_turns)

    ids=[p.id for p in players]

    ratio=[i['won'] for i in history].count('red')/len(history)

    id=ids[0]

    a=[i[id]['balance'] for i in history]

    plt.plot(a)
    plt.show()

    print(history)
    print(a)
    print(ids)
    print(ratio)