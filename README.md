# Pong 2.0 (Warning: Flashing lights)

#IMPORTANT: If ball speed is too slow/fast, read directions below on how to fix.

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
zcontrol-a1  (Ball speed Y axis)
***Default = .36 <br />
zcontrol-a2  (Ball speed X axis)
***Default = .39 <br />
zcontrol-a3  (Ball speed X axis reset speed reset after any player scores)  
***Default = .39 <br />
zcontrol-a4  (Ball speed Y axis speed reset for Player A) 
***Default = .39 <br />
zcontrol-a5  (Ball speed Y speed axis reset for Player B && Reverses ball direction when Player B scores)  
***Default = -.39 <br />

#### Paddle controls:
zcontrol-a6  (Player A move paddle UP) <br />
zcontrol-a7  (Player A move paddle DOWN) <br />
zcontrol-a8  (Player B move paddle UP) <br />
zcontrol-a9  (Player B move paddle DOWN) <br />
#### Round limit:
zcontrol-b1  (Round limit for Player A to win) ***Default = 3 <br />
zcontrol-b2  (Round limit for Player B to win) ***Default = 3 <br />

Ball speed:
If ball speed is too slow/fast, adjust declarations of variables as needed.
Find and adjust all (5) variables via ctrl+f or command-f: <br/>
zcontrol-a1 <br />
zcontrol-a2  <br />
zcontrol-a3 <br />
zcontrol-a4 <br />
zcontrol-a5 <br />

Number of rounds until game completion <br />
Using ctrl+f/cmd+f search for the commented "zcontrol-b2" and "zcontrol-b3" in the program. Currently set for 3 rounds. Output of winner displayed on screen as well as sent to console.

Reset game wins <br />
To reset the game win counter that is displayed at the end of the game, delete both .PICKLE files in root directory. 

## Updates Added: <br />

-Super attack (Player can automatically return the ball chaotically) - Current odds of cast are 1/15 <br />

-Nuclear attack (Player can manually return the ball chaotically) - Slam key at exact moment ball hits paddle. Ball enlarges and becomes almost unstopable. <br />

-When ball collides with paddle, ball's returning y axis is now random

-Ball X and Y axis are both random at start

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

-Sound effects added for game finish

-Keeps lifetime count of player wins via serialization/pickling

Updates coming soon:

-Power ups: Randomly or condition generated items that if touched with paddle will either hurt or help player. Such as paddle   size reduction/enhancement, multi paddle, multi ball that doesn't return to hurt sender.

-Option for different window sizes. Maybe 1 60% larger and another at a large 16:9 ratio. All elements would need pushed out to new positions, adjust target areas, add option to startup screen (before countdown) to choose screen size.

-Option to choose screen color (along with screen size) lay on white screen (instead of black).

-Sync game speed with a constant of some sort. The system clock?


*Turtle run Pong game that's been heavily remixed and improved upon in some areas*
*Sounds from Zapsplat.com*
