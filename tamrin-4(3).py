import re
import matplotlib.pyplot as plt
import numpy as np
class Player:
    def __init__(self, health, cards):
        self.health = health
        self.cards = cards
        self.score = 0
    def play_card(self, opponent, cardd1, cardd1_in, cardd2_in, cardd2):
        my_damage = self.cards[cardd1_in][cardd1]
        opponent_damage = opponent.cards[cardd2_in][cardd2]
        Player1.health -= opponent_damage
        opponent.health -= my_damage
        if my_damage > opponent_damage:
            Player1.score += 1
        if my_damage < opponent_damage:
            Player2.score += 1
try:
    name1,name2 = input().split()
    health1, health2 = map(int,input().split())
    damage1,damage2,damage3 = map(int,input().split())
    Player1 = Player(health1, [{'A': damage1}, {'B': damage2}, {'C': damage3}])
    Player2 = Player(health2, [{'A': damage1}, {'B': damage2}, {'C': damage3}])
    letter_index = {'A':0, 'B':1, 'C':2}
    card1,card2 = input().split()
    Player1.play_card(Player2, card1, letter_index[card1], letter_index[card2], card2)
    card3,card4 = input().split()
    Player1.play_card(Player2, card3,letter_index[card3], letter_index[card4], card4)
    card5,card6 = input().split()
    Player1.play_card(Player2, card5,letter_index[card5], letter_index[card6], card6)

    print(f"{name1} -> Score: {Player1.score}, Health: {Player1.health}")
    print(f"{name2} -> Score: {Player2.score}, Health: {Player2.health}")
except:
    print('Invalid Command.')
    # player_score = {}
    # player_score[name1] = Player1.score
    # player_score[name2] = Player2.score

    # listx = list(player_score.keys())
    # listy = list(player_score.values())
    # with open('result.txt', 'a')as file:
    #     for item in listx:
    #         file.write(f"{item} ")
    #     for item in listy:
    #         file.write(f"{item} ")
    #     file.close()
        
    # f = open("result.txt", "r")
    # aa = f.read()
    # n = re.findall('[a-zA-Z]+', aa)
    # m = re.findall('[0-9]+', aa)
    # x = np.array(n)
    # y = np.array(m)
    # plt.bar(x,y)
    # plt.show()
