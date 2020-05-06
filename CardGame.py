import random
import flask
import os
from flask import Flask
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)

house = {"hearts": 'H', "diamonds": 'D', "spades": 'S', "clubs": 'C'}
cards = ['A', 'K', 'Q', 'J', '7', '8', '9', '10']
points = {'A': 1, '9': 2, '10': 1, 'J': 3, 'K': 0, 'Q': 0, '7': 0, '8': 0}
maps_of_card_point = {}
shuffl_cards = []
player1 = []
player2 = []
player3 = []
player4 = []
all_players = {}

@app.route('/shufflecards')
def shuffle_cards_for_players():    
    for k, v in house.items():
        for i in range(len(cards)):
            for x, y in points.items():
                if x == cards[i]:
                    maps_of_card_point[cards[i]+v] = y

    print(maps_of_card_point)
    print(len(maps_of_card_point))   
    for k in maps_of_card_point.keys():
        shuffl_cards.append(k)

    for i in range(1, 50):
        random.shuffle(shuffl_cards)
    for i in range(len(shuffl_cards)):
        if i % 4 == 1:
            player1.append(shuffl_cards[i])
        elif i % 4 == 2:
            player2.append(shuffl_cards[i])
        elif i % 4 == 3:
            player3.append(shuffl_cards[i])
        elif i % 4 == 0:
            player4.append(shuffl_cards[i])
    return 'DOne shuffling'

def listToDict(lst):
    op = { i : lst[i] for i in range(0, len(lst) ) }
    return op

@app.route('/player1')
def player1cards():
    return json.dumps(player1)

@app.route('/player2')
def player2cards():
    return json.dumps(player2)
    
@app.route('/player3')
def player3cards():
    return json.dumps(player3)

@app.route('/player4')
def player4cards():
    return json.dumps(player4)

@app.route('/allplayers')
def allplayer():
    all_players['player1']= player1
    all_players['player2']= player2
    all_players['player3']= player3
    all_players['player4']= player4
    return all_players




if __name__ == "__main__":
    app.run('0.0.0.0')
