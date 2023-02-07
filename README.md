# My Bots

### Fitness Function
The perfect robot climbs the stairs in the negative x-direction.
My fitness function remains the final x-coordinate of the robot, 
as the stairs would inhibit robots that cannot climb them.

### What each file does:

#### analyze.py
Draws graphs of movement (no longer used).

#### constants.py
Contains all constants used across the directory.

#### generate.py
Creates the world (no longer used)

#### hillclimber.py
Selects randomly among multiple generations (no longer used).

#### motor.py
Sets the motor for all joints.

#### parallelhillclimber.py
Selects randomly across a population among multiple generations.

#### robot.py
* Calls the sensors and motors of the robot to get it to sense then act.
* Evaluates the fitness of the robot (IMPORTANT).

#### search.py 
Runs the entire evolution cycle.

#### sensor.py
Determines if a body part is touching the floor.

#### simulate.py
Automates running a single round of the simulation.

#### simulation.py
Runs a single round of the simulation.

#### solution.py
* Creates the world, the robot's body, and the robot's brain.
* Randomly mutates one sensor/motor pair.
* Starts the simulation and evaluates the fitness.

#### world.py
Loads the world and the floor plane.