# Pizzabot Instructor
## Version
1.0.0
## Requirements
Python 3.9
## Description  
Pizzabot is a robot that delivers pizza to the houses in the neighborhood. It sees this world as a grid, the nodes of which are houses. The task of this program is to instruct the robot to deliver pizza to all the houses marked on the grid.  
## Input
For the program to work, a string of input data is required, which looks like this `5x5 (0,0) (2,1)`. Where `5x5` is the grid size and `(0,0) (2,1)` is the list of delivery points. To avoid errors, follow this pattern of input data `FIELD_LENGHTxFIELD_HEIGHT (x1,y1) (x2,y2) ...`
## How does it work?
The program tries to parse a line of input data and return a list of commands for the robot and in cases of incorrect input data format inform the user about it. The robot is under development and does not understand so many commands yet. Here is a list of what it understands now:  
- `N` - move North
- `E` - move East
- `S` - move South
- `W` - move West
- `D` - drop pizza  

The robot always starts its journey from the point `(0,0)` and passes through all the specified delivery points. The point `(0,0)` corresponds to the location of the origin in the Cartesian plane. The end point of the route is one of the delivery points (the robot does not return to the starting point).

## How to run ?
After downloading, go to the root folder of the project and open the console in it, then run `pizzabot.py` is like a regular python script with arguments:
- For macOS and Linux: `python3 pizzabot.py "args"`
- For Windows: `python pizzabot.py "args"`  

Quotation marks are required!
## Output
In case of successful execution of the program, a line containing commands for the robot is output to the console. For the previous example, it will look like this: `DNEED`
## Challenge
To complete the challenge, enter this line as input data `5x5 (0, 0) (1, 3) (4, 4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3) (4, 1)`. The result should be `DNNNEDNEEEDSSDDSWWWWDNEEEDNWDSSEED`.
