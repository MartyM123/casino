import random
import matplotlib.pyplot as plt

def generate():
    return random.choices(['red', 'black', 'green'], (18, 18, 1))[0]

def generate_r_b():
    return random.choice(['red', 'black'])

generate = generate_r_b

class Player:
    def __init__(self, money:int=50):
        self.id = str(random.randint(1, 10**6))
        self.money=money
        self.alive=True

    def decision_function(self):
        return random.choice(['red', 'black'])

    def make_decision(self):
        amount=10
        return self.decision_function(), amount

    def on_win(self):
        pass

    def on_lose(self):
        pass

    def __iadd__(self, other):
        self.money += other

    def __isub__(self, other):
        self.money -= other

    def __str__(self):
        return f'model id: {self.id}, money: {self.money}'

def create_history(players, n_turns):
    # set parameters
    history = []

    #create history with known victory colors
    for i in range(n_turns):
        history.append({'turn': i})


    for player in players:
        if player.alive:
            for turn in history:
                tip, amount = player.make_decision()
                amount=min(player.money, amount) #to be sure that player won't bet more than he has
                won=generate()
                if tip == won:
                    player += amount
                    player.on_win()
                    turn[player.id] = {'tip': tip, 'amount': amount, 'balance': player.money}
                    turn[player.id]['won'] = won
                else:
                    player -= amount
                    player.on_lose()
                    turn[player.id] = {'tip': tip, 'amount': amount, 'balance': player.money}
                    turn[player.id]['won'] = won
    return history

if False:
    n_turns = 100 #number of turn of rulet
    n_players = 2 #number of players

    players = []
    #create players
    for i in range(n_players):
        players.append(Player())

    history = create_history(players, n_turns)

    ids = [p.id for p in players]

    ratio = [i['won'] for i in history].count('red')/len(history)

    id = ids[0]

    a = [i[id]['balance'] for i in history]

    plt.plot(a)
    plt.show()

    print(history)
    print(a)
    print(ids)
    print(ratio)
