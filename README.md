##Snake Game

####Coding of the AI
Now we can get started with the coding the actual AI.

We will implement the AI using a neural network. There are several kinds of networks we can use for this task. We will use a simple form of network called a Feedforward nural network.

It means that we construct a network where the nodes never form a circle. We pass in data in one end, into something that is called input nodes. The passes through the network layers and gives us an output at the other end.

We will form a network consisting of three layers. 

The input layer is formed by 11 nodes. The reason there are 11 nodes is that we will use an input that conosist of 11 values. 
We will soon come to why we ended up with 11 values.

The output layer will consist of three nodes. The reason for this is that what we need from the AI is an action, and as we saw in the previsous branch play_step_ai wants an input consisting och three values.

This is an illustration of a feedforward network.

![Feedforward Neural Network](./img/Feed_forward_neural_net.gif)

As we can see, the information moves only in one direction. We can also see that betwen the input and output layer is a hidden layer. We can exepriment with the number of nodes in this layer to find something that works for our task. We are not limited to just three layers either, we can, if we want, add more hidden layers to our network.

###Forming the Input Data
The data that we will feed the network with is some information about the state of the game after each step. 

This will consist of 11 zeros and ones. We will not tell the network the meaning of these values. It will need to figure that out by itself.

The input data will consist of three parts.

#####Danger Path
The first three values represents if a move in a given direction will result in death of the snake.

A 1 represents death if we move in that direction and 0 that this move is safe.

If the snake is moving to the left and it's head is just one tile from the left wall, a move straight ahead would mean death. So if there is a 1 in the first location it represent that we will die if we move forward in the direction we currently moving in.

The second value will tell us the result of right turn, and the third value the result of a left turn.

Here are some combinations of these first three values as an example:

0, 0, 0 = All directions are safe
1, 0, 0 = Right and left are safe but straight ahead will kill the snake
1, 0, 1 = Straight and a left turn will kill the snake, but a right turn is safe
1, 1, 0, = Straight and a right turn will kill the snake, but moving to the left is safe
1, 1, 1 = You are screwed

#####Current Direction
The next four values represents the current direction.
Only one of these can be 1 at any given time. The order of the values are:

left, right, up, down

so the combination

0, 1, 0, 0

mean that the snake is traveling to the right

0, 0, 1, 0

mean that the snake is heading up.

#####Fruit Location
The last 4 values represents where the fruit is located in relation to the head of the snake. It is not an exact location. The first two values tells us if the fruit is to the left or to the right. The last two values tells us if the fruit is above or below us.

Some examples

1, 0, 0, 1 = The fruit is to the left and below us
0, 0, 1, 0 = We are in the same column as the fruit but it is above us
0, 1, 0, 0 = We are on the same row as the fruit but it is to our right.

######All Values Together
If we put all these values together we can get something like this

[1, 1, 0,
 0, 1, 0, 0,
 1, 0, 1, 0]

 As we can see, we got 11 values. These can be interpreted as:

 You will die if you move straight ahead or turn to the right, but turning left is OK. (First three values)

 You are currently moving in the right direction. (Next four values)

 The fruit is to your left and above you. (The last four values)

 We know the meaning of these values, but the AI don't.

 ####Long and Short Memory
 The AI will also work with something that is called a long and short memory.

 The short memory is just the last step is took. The long memory is a number of previsous steps, up to a limit that we set. We will use up to a maximum of 1,000 steps prior to where we are now.

 The network will "replay" the last step it took to evaluate the outcome of it's action. We will tell it the outcome of that move (death or no death) and the reward we got from that move.

 We will also store each move and its outcome in the long memory.

 When the snake dies it will replay all moves in the long memory and learn from it.