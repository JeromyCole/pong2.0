# Pong 2.0

WARNING: FLASHING LIGHTS

## Controls
### Player A:

Up - 'W' || 'w' <br />
Down - 'S' || 's' <br />
Special Attack - 'Space' (Only works when you hit the key exactly when the ball hit the paddle) <br />

### Player B:

Up - '8' <br />
Down - '2' <br />
Special Attack - '0' (Only works when you hit the key exactly when the ball hit the paddle) <br />

## zcontrol (Find code with CTRL+F or COMMAND-F using relevant "zcontrol-xx" code below): <br />

Locate Pong controls via Find/Search: <br />
zcontrol-a1  (Ball speed y axis)  ***Default = .36 <br />
zcontrol-a2  (Ball speed x axis)  ***Default = .39 <br />
zcontrol-a3  (Ball speed y axis reset after Player A scores)  ***Default = .36 <br />
zcontrol-a4  (Ball speed x axis reset after Player A scores)  ***Default = .39 <br />
zcontrol-a5  (Ball speed y axis reset after Player B scores)  ***Default = .36 <br />
zcontrol-a6  (Ball speed x axis reset after Player B scores)  ***Default = .39 <br />
zcontrol-a7  (Player A move paddle UP) <br />
zcontrol-a8  (Player A move paddle DOWN) <br />
zcontrol-a9  (Player B move paddle UP) <br />
zcontrol-b1  (Player B move paddle DOWN) <br />
zcontrol-b2  (Round limit for Player A to win) ***Default = 3 <br />
zcontrol-b3  (Round limit for Player B to win) ***Default = 3 <br />

### Ball speed:
If ball speed is too slow/fast, adjust declarations of variables ball.dx and ball.dy as needed: <br />
Find and adjust all (6) variables via ctrl+f or command-f: <br />
zcontrol-a1 <br />
zcontrol-a2  <br />
zcontrol-a3 <br />
zcontrol-a4 <br />
zcontrol-a5 <br />
zcontrol-a6 <br />

### Number of rounds until game completion <br />
CTRL+F/Command+F "zcontrol-b2" and "zcontrol-b3". Currently set for 3 rounds. Output of winner displayed on screen as well as sent to console.

## Updates Added: <br />
-Super attack (Player can automatically return the ball chaotically) - Current odds of cast are 1/15 <br />

-Nuclear attack (Player can manually return the ball chaotically) - Slam key at exact moment ball hits paddle. Ball enlarges and becomes almost unstopable. <br />

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


## Updates Coming:

-Paddle speed and direction effecting ball speed and direction

-Power ups: Randomly generated items that if touched with paddle will either hurt or help player. Such as paddle size  reduction/enhancement, multi paddle, multi ball that doesn't return to hurt sender.
 and more.

-Random ball direction at startup

-Give option for larger resolution gameplay.

-Paddle size increases when score point?


This is a common Turtle run Pong game that's been remixed and improved upon in some areas. 
