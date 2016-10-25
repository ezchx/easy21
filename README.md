Course Slides
http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html

Assignment
http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/Easy21-Johannes.pdf

Description

1)	The player and dealer are each dealt 1 card
2)	The player hits or stands based on epsilon greedy exploration strategy
    a.	Epsilon = 100 / (100 + N(s)) where N(s) is the number of times the state has been visited
    b.	If a random number from 0-1 > epsilon then use the prior best action, if not pick a random action.
        So as N(s) increases, epsilon decreases and you are more likely to follow the prior best action.
3)	If the player stands before busting, then the dealer draws until > 17 or <  1
4)	At the end of each hand, the Q matrix is updated for each state / action combination as follows:
    a.	Q new = Q old + (alpha * (hand reward  - Q old))

  Dealer	Player	Action		N	    Alpha	  Q old 	Q update
  10    	7	      Hit		    15	  1/15	  0.223	  0.053
  10	    16	    Hit		    10	  1/10	  0.312	  0.070
  10	    18	    Stand		  7	    1/7	    0.501	  0.071
  17	    18	    Win +1		2	    1/2


Many thanks to https://github.com/xrz000/Easy21
