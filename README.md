## Snake Game

#### The Final Game
In this branch you can find an example of the final AI program that will train the model.

After about 90 - 100 games it will stop developing any further.

##### Improvements
If you want this AI to get better you must give the chance to do so. The first step would to somehow let it know that it is making a 'dead-end street' with its body, and by that trapping itself. This can either be done by letting the AI know about its body location. An other alternative would be to use a shortest path algorithm, such as A*, to see if there is a way for the head to reach the fruit if we move in one direction.

The problem with both of these options will be that what might look like a trap at the moment might not be a trap if we move a number of steps, as the tail is moving too. So what might look like a dead end might in a few steps open up.

Hope you had fun
