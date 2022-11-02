##Snake Game

####The step1 Branch
The first thing we need to do is to setup the game to be able to be played by the AI.

####Additions to the SnakeGame Class
Open the game.py file. We already have a method called play_step_human in this class. If you look below it, you will now see a new, method called play_step_ai.

The AI will later decide on a step, and this step can be one of three. It can decide to keep on going in the direction it is already heading, it can turn right, or it can turn left. When the AI has decided on its move, it will be passed to this new method as action.

#####The Action
The action passed to the method will be in the form of a list containing three integers. The integers in the list can be either 0 or 1.
The location of a 1 in this list will tell us the desired move. The actions is as follows:

[1, 0, 0] -> Keep on going in the current direction
[0, 1, 0] -> Turn right
[0, 0, 1] -> Turn left

#####Set the Direction of the Snake
If you look what happens in the human play method when a user press any of the arrow keys you will see that the snake direction is controlled by setting self.direction to one of the values in the Direction enum.

The differens between how a human is controlling the snake and how the AI does it is that the action we are getting is either keep on going, go left, or go right and is not matched to the directions given when a human is pressing any of the arrow keys.

To be able to control the snake we will need to translate the action into a direction. The problem here is that the direction is dependent of the current direction of the snake.

If the snake is heading to the right and the action is turn right the new direction will be down. It the snake, on the other hand is going left and we ask it to turn right, the new direction will be up.

Check the table below to see how the current direction and action is translated into a new direction.

| Current Direction | Action | New Direction |
|---|---|---|
| Left | Right | Down |
| Left | Left | Up |
| Down | Right | Right |
| Down | Left | Left |
| Right | Right | Up |
| Right | Left | Down |
| Up | Right | Left |
| Up | Left | Right |

We will do this translation by the use of a list containing all four possible directions in the order Right, Down, Left, and Up. That is a clockwise rotation start at the right direction. 

The first thing we will do is to extract the index in this list of the current direction of the snake.

The action list is giving us two possible moves we need to consider as the keep on going action actually means do nothing.

We will compare our action array to either a right or a left turn. 

We now know the two things we need to know, the current direction and if we want to turn left or right. The only thing we need to do to get the new direction if to add 1 to the index of the current direction variable, if the action tells us to turn right, and subtract 1 from the index variable if we want to turn left.

To make sure we stay within the clockwise direction list with our new index we perform a modulus by the length of the list.

We can now use this new index to look up our new direction from the list of directions.

#####Move the Snake
After that we can call the self._move method to make the snake move one step in the new direction.

#####Calculate the Reward
As we will be using Reinforcement Learn to thrain the AI we will need to have a reward for each move.

The reward is calculated with positive values if the snake does something we think is a good move, and a negative value if it does something bad.

To know how we shoudl reward the AI for this move we must first evaluate the result of the move.

It is possible that the move resulted in a collision. That is a bad outcome, so the reward for the last move will be -10.

Sometimes the snake will end up in an enless loop, or just move around doing anything useful. We will consider this a useless run, kill the snake and give a reward of -5. We keep track of how many iterations (that is actually how many times we visited this method) since we last got a positive reward. If this value is larger than 100 * the length of the snake it is time to kill the snake and start over. 

We take the snakes lenght into consideration here as a successful run with a long snake mean that the snake must take a longer path to reach the fruit, so it needs more steps before it gets rewarded.

The only time the AI gets a positive reward is when it reaches the fruit. In this case we will reward the AI with a positive 10.

We can play around with this positive reward to see if it improves training of the AI.

One option would to to, besides the 10 point reward for reaching the fruit, give it another positive reward for moving in the right direction. 

We could for example calculate the Eucledian distance between the snakes head and the fruit. We could use this value to calculate a reward in the range of, for example 0.1 and 5.0. A higher value mean it is closer to the fruit. This could be a way for the AI to learn to head for the fruit faster than if we did not give it this reward. 

If you try this remember to give it a larger reward when it actually reaches the fruit, and also remeber not to reset the iterations_since_reward counter for this reward as it will reset that counter each step. We only want to reset it when the snake gets the fruit.

#####What the Method Returns
This method returns three values. The first one is a boolean indicating of we should end the game or not. False mean we survived, keep on going and True is an indication that we are dead.

The scond value returned by the method is the reward for this move, and the last value is the current score.

#####Test the Code
To test our new method, run ai_snake.py. It contains some hard coded actions that we send to the play_step_ai method, to see it in action.

#####Next Step
Now we are done with the boilerplate code for this project. Checkout the **ai** branch, and we are ready to code some cool stuff.