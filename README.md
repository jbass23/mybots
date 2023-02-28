# Evolving 3D Robot

## Basic Idea
This program is designed to create a random, three-dimensional robot out of non-overlapping links and joints. Then, it
"evolves" the creature through a Parallel Hill Climber method: a population of 50 (or less/more) robots are created
randomly, then are randomly mutated from generation to generation. If a mutation improves fitness, it is kept. If it
does not, it is disgarded. The final shown robot is the one that performs the best among the evolved population.

## Running the Program
Download the files and type `python3 search.py X` into your terminal to run, where _X_ is replaced with any number to
select the seed (it runs `np.random.seed(X)`). A python pop-up should appear with your random creature. Run again for a
new creature, and select a different seed, then back to the original to get replicate your ludobots. For my testing, I
used seeds 1, 2, 3, 4, and 5 (the image is saved to a file called "fitness*X*.png). If you also use seeds 1-5, you can
afterwards run `python3 analyze.py` to create a graph of the fitness of the best creature for any given generation among
those five seeds. 

## Images/Videos
### Creating a Creature:
![A diagram of the body generating process](images/diagram.jpg "Body Diagram")

### Mutating a Creature:
![A diagram of the body mutation process](images/mutation.jpg "Mutation Diagram")

### Example Creatures:
![A picture of one random creature](images/creature1.png "Random Creature #1")
![A picture of another random creature](images/creature2.png "Random Creature #2")

### Example of Creature Evolution:
<https://youtu.be/hoS8XTKo2eQ>


## Credits
* Ludobots from Dr. Josh Bongard and the University of Vermont: <https://www.reddit.com/r/ludobots/wiki/installation/>
* PyroSim: <https://www.thunderheadeng.com/pyrosim>
* Professor Sam Kriegman and Northwestern University's COMP_SCI 396: Artificial Life
* Inspiration for work and diagrams from Karl Sims' research