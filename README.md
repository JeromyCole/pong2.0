Pong 2.0

WARNING: FLASHING LIGHTS

Controls
Player A:

Up - 'W' || 'w'
Down - 'S' || 's'
Special Attack - 'Space' (Only works when you hit the key exactly when the ball hit the paddle)

Player B:

Up - '8'
Down - '2'
Special Attack - '0' (Only works when you hit the key exactly when the ball hit the paddle)

zcontrol (Find code with CTRL+F or COMMAND-F using relevant "zcontrol-xx" code below):

Locate Pong controls via Find/Search:
zcontrol-a1  (Ball speed y axis)  ***Default = .36
zcontrol-a2  (Ball speed x axis)  ***Default = .39
zcontrol-a3  (Ball speed y axis reset after Player A scores)  ***Default = .36
zcontrol-a4  (Ball speed x axis reset after Player A scores)  ***Default = .39
zcontrol-a5  (Ball speed y axis reset after Player B scores)  ***Default = .36
zcontrol-a6  (Ball speed x axis reset after Player B scores)  ***Default = .39
zcontrol-a7  (Player A move paddle UP)
zcontrol-a8  (Player A move paddle DOWN)
zcontrol-a9  (Player B move paddle UP)
zcontrol-b1  (Player B move paddle DOWN)
zcontrol-b2  (Round limit for Player A to win) ***Default = 3
zcontrol-b3  (Round limit for Player B to win) ***Default = 3

Ball speed:
If ball speed is too slow/fast, adjust declarations of variables ball.dx and ball.dy as needed:
Find and adjust all (6) variables via ctrl+f or command-f:
zcontrol-a1
zcontrol-a2
zcontrol-a3
zcontrol-a4
zcontrol-a5
zcontrol-a6

Number of rounds until game completion
CTRL+F/Command+F "zcontrol-b2" and "zcontrol-b3". Currently set for 3 rounds. Output of winner displayed on screen as well as sent to console.

Updates Added:
-Super attack (Player can automatically return the ball chaotically) - Current odds of cast are 1/15

-Nuclear attack (Player can manually return the ball chaotically) - Slam key at exact moment ball hits paddle. Ball enlarges and becomes almost unstopable.

-Start up screen with countdown

-Paddle collision counter

-When ball collides with paddle, ball's returning y axis is now random

-Colored paddles that when player scores turn ball into their paddle's color.

-Reset ball speed to starting speed after each round.

-Game winner screen specifying which player won. Current  game ends after 3 rounds are won.

-Flash screen with player's color when scored

-Stop paddles from going off the screen.

-Fixed paddle collisions where ball collides with paddle incorrectly

-Paddle movements automove on key hold

-Progressively increased speed upon ball hit (*Recycled code someone elsecame up with)


Updates Coming:

-Paddle speed and direction effecting ball speed and direction

-Power ups: Randomly generated items that if touched with paddle will either hurt or help player. Such as paddle size  reduction/enhancement, multi paddle, multi ball that doesn't return to hurt sender.
 and more.

-Random ball direction at startup

-Give option for larger resolution gameplay.

-Paddle size increases when score point?


This is a common Turtle run Pong game that's been remixed and improved upon in some areas. 
