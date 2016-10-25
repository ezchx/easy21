import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from easy21 import step


## From Sutton and Barto ##
## Generate an episode using exploring starts and pi ##
# for each pair s,a appearing in the episode:
#   R <- return following the first occurrence of s,a
#   Append R to R(s,a)
#   Q(s,a) <- average(R(s,a))
# for each s in the episode:
#   Pi(s) <- argMax Q(s,a)


N0 = 100
hands = 100000
gamma = 1
N = np.zeros([10, 21, 2]) # total visits to each state / action combination
Q = np.zeros([10, 21, 2]) # reward for each state / action combination
V = np.zeros([10, 21]) # max reward for each state


# epsilon greedy exploration strategy - based on https://github.com/xrz000/Easy21
def epsilon_greedy(N0, N, Q, dealer, player):
    
    epsilon = N0 / (N0 + np.sum(N[dealer - 1, player - 1, :])) # as visits to the state goes up, epsilon goes down, and you are more likely to use the prior best action (exploit)
    explore = np.random.uniform(0, 1)

    if explore > epsilon:
        action = np.argmax(Q[dealer - 1, player - 1, :]) # use the prior best action (exploit)
    else:
        action = np.random.randint(0, 2) # try a random action hit = 0, stick = 1 (explore)

    return action


# let's play some cards!
for i in range(hands):
    
    # player and dealer each draw one black card
    dealer = np.random.randint(1, 11)
    player = np.random.randint(1, 11)
    deal = ([dealer, player], 0)

    # play one hand
    history = []
    reward = None
    while reward == None:
        
        dealer = deal[0][0]
        player = deal[0][1]
        action = epsilon_greedy(N0, N, Q, dealer, player)
        N[dealer-1, player-1, action] += 1
        deal = step([dealer, player], action)
        reward = deal[1]
        history.append(([dealer, player], action, reward))

    # update the Q matrix for this hand - based on https://github.com/xrz000/Easy21
    Gt = 0
    for j, ([dealer, player], action, reward) in enumerate(reversed(history)): # backtrack from the end of the hand to the beginning
        alpha = 1.0 / N[dealer - 1, player - 1, action] # update factor as per the assignment. As you have more visits to the state, the update factor decreases.
        if reward == None:
            reward = 0
        Gt = gamma * Gt + reward # cumulative reward for each move in the hand. Since the reward is only given at the end of the hand, this is the same for all states.
        Q[dealer - 1, player - 1, action] += alpha * (Gt - Q[dealer - 1, player - 1, action]) # update the Q matrix based on the cumulative reward


V = np.amax(Q, axis=2)


# plot value function - from https://github.com/xrz000/Easy21
x = np.arange(1, 11)
y = np.arange(1, 22)
xs, ys = np.meshgrid(x, y)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(xs, ys, V.T, rstride=1, cstride=1)
plt.show()
