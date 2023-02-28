import constants as c
import numpy as np
import matplotlib.pyplot


fitnessValues = []
bestValues = []
for i in range(5):
    fitnessValues.append(np.load(f"data/fitnessValues{i+1}.npy"))
    arrayOfBest = []
    for k in range(c.numberOfGenerations + 1):
        best = 0
        for j in range(c.populationSize):
            if fitnessValues[i][j][k] > fitnessValues[i][best][k]:
                best = j

        arrayOfBest.append(fitnessValues[i][best][k])

    bestValues.append(arrayOfBest)

for i in range(len(bestValues)):
    matplotlib.pyplot.plot(bestValues[i], label=f"population #{i+1}")
matplotlib.pyplot.title("Members With Best Fitness Across 5 Generations")
matplotlib.pyplot.xlabel("Number of Generations")
matplotlib.pyplot.ylabel("Fitness")
matplotlib.pyplot.savefig("graphs/fitnessBests.png", format="png")
