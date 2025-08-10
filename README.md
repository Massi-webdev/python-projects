**Famous Pong game**
In this section, I decided to create a popular game named pong game using all material I have learned in this unit.

Here are screenshots of my code with comments to explain the logic.

Firstly, import turtle #let's start by importing turtle, we start by defining the window properties and name. Afterwards, we create all drawing objects, we will use in the game (2paddles and a ball)
Then, we create score and display and pen object to write score on screen.

Second part is to create functions to move paddles and then we create bindings functions and we use event listener like to tell windows to listen to event

lastly and most importantly, the game logic. We start by keeping the game running with an infinite loop. Then we move the ball by getting the current position using xcor and add the horizontal or vertical change. 
Afterwards, we manage ball collisions for example if ball is at extreme top, it is stopped and reversed. Additionally, we manage scoring and updating it when losing/winning by handling ball paddle collisions and see if ball is near paddleB position 340-350 range and see if ball position is within the paddle centre. If true then stop the ball and reverse it.
