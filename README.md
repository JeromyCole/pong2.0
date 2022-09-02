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

### All "adjustable" aspects of the game have commented code you can find quickly via ctrl+f or cmd+f and search for the below code. Example: zcontrol-a1

Locate Pong controls via Find/Search: <br />
#### Change speed:
zcontrol-a1  (Ball speed y axis)  ***Default = .36 <br />
zcontrol-a2  (Ball speed x axis)  ***Default = .39 <br />
zcontrol-a3  (Ball speed y axis reset after Player A scores)  ***Default = .36 <br />
zcontrol-a4  (Ball speed x axis reset after Player A scores)  ***Default = .39 <br />
zcontrol-a5  (Ball speed y axis reset after Player B scores)  ***Default = .36 <br />
zcontrol-a6  (Ball speed x axis reset after Player B scores)  ***Default = .39 <br />
#### Paddle controls:
zcontrol-a7  (Player A move paddle UP) <br />
zcontrol-a8  (Player A move paddle DOWN) <br />
zcontrol-a9  (Player B move paddle UP) <br />
zcontrol-b1  (Player B move paddle DOWN) <br />
#### Round limit:
zcontrol-b2  (Round limit for Player A to win) ***Default = 3 <br />
zcontrol-b3  (Round limit for Player B to win) ***Default = 3 <br />

Ball speed:
If ball speed is too slow/fast, adjust declarations of variables ball.dx and ball.dy as needed: <br />
Find and adjust all (6) variables via ctrl+f or command-f: <br />
zcontrol-a1 <br />
zcontrol-a2  <br />
zcontrol-a3 <br />
zcontrol-a4 <br />
zcontrol-a5 <br />
zcontrol-a6 <br />

Number of rounds until game completion <br />
Using ctrl+f/cmd+f search for the commented "zcontrol-b2" and "zcontrol-b3" in the program. Currently set for 3 rounds. Output of winner displayed on screen as well as sent to console.


## Updates Added: <br />

-Super attack (Player can automatically return the ball chaotically) - Current odds of cast are 1/15 <br />

-Nuclear attack (Player can manually return the ball chaotically) - Slam key at exact moment ball hits paddle. Ball enlarges and becomes almost unstopable. <br />

-When ball collides with paddle, ball's returning y axis is now random

-Start up screen with countdown

-Ball now momentarily squishes when it hits a paddle

-Ball wobbles when moving through air

-Paddle collision counter

-Colored paddles that when player scores turn ball into their paddle's color

-Game winner screen specifying which player won. Current  game ends after 3 rounds are won

-Reset ball speed to starting speed after each round

-Flash screen with player's color when scored

-Stop paddles from going off the screen

-Fixed paddle collisions where ball collides with paddle incorrectly

-Progressively increased speed upon ball hit (*Recycled code someone else came up with)

-Nuclear attack has additional effect where its changes size when deployed and hit afterward if in succession

-Sound effects added for nuclear attacks

-Sound effect added for game finish

Updates Coming:

-Power ups: Randomly or condition generated items that if touched with paddle will either hurt or help player. Such as paddle  size reduction/enhancement, multi paddle, multi ball that doesn't return to hurt sender.
 and more.

-Give option for different window sizes. Maybe 1 60% larger and another at a large 16:9 ratio. All elements would need pushed out to new positions, adjust target areas, add option to startup screen (before countdown) to choose screen size.

-Give option to choose screen color (along with screen size) lay on white screen (instead of black)

*Turtle run Pong game that's been heavily remixed and improved upon in some areas*
*Sounds from Zapsplat.com*
