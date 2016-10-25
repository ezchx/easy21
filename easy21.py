import numpy as np


# draw a card
def draw(hand):
    color = np.random.randint(1, 4)
    value = np.random.randint(1, 11)

    if color == 1:
        value = -value

    hand = hand + value

    return hand


# step function
def step(s, a):
    dealer = s[0]
    player = s[1]
    reward = None

    if a == 0: # player hits

        player = draw(player)

        if player > 21 or player < 1:
            reward = -1

    if a == 1: # player sticks

        while dealer > 0 and dealer < 17 :
            dealer = draw(dealer)

        if dealer < 1 or dealer > 21 or (dealer >= 17 and dealer < player):
            reward = 1

        if dealer >= 17 and dealer <=21 and dealer > player:
            reward = -1

        if dealer >= 17 and dealer <=21 and dealer == player:
            reward = 0

    return [dealer, player], reward
