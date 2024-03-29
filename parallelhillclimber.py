import numpy as np
import constants as c
from solution import SOLUTION
import copy
import os
import matplotlib.pyplot as mpl
import pickle


class PARALLEL_HILL_CLIMBER:
    def __init__(self, seed):
        self.seed = seed
        np.random.seed(self.seed)

        os.system("rm body*.urdf")
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        os.system(f"rm pickles/run{self.seed}*.pkl")

        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

        self.fitnessList = np.zeros((c.populationSize, c.numberOfGenerations + 1))
        self.bestFitness = float('-inf')

        self.pickleCount = 0

    def Evolve(self):
        self.Evaluate(self.parents)
        for member in range(c.populationSize):
            self.fitnessList[member][0] = self.parents[member].fitness

        self.Pickle_Solution(self.Find_Fittest())

        for currentGeneration in range(c.numberOfGenerations):
            print(f"Generation #{currentGeneration + 1}:")
            self.Evolve_For_One_Generation()
            for member in range(c.populationSize):
                self.fitnessList[member][currentGeneration + 1] = self.parents[member].fitness

            fittest = self.Find_Fittest()
            if self.parents[fittest].fitness < self.bestFitness:
                self.Pickle_Solution(fittest)

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()

    def Select(self):
        for i in self.parents:
            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i] = self.children[i]

    def Print(self):
        print()
        for i in self.parents:
            print(f"parent: {self.parents[i].fitness}; child: {self.children[i].fitness}")
        print()

    def Show_Best(self):
        fittest = self.Find_Fittest()

        self.parents[fittest].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation("DIRECT")

        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()

    def Save_Data(self, x):
        for i in range(c.populationSize):
            for j in range(c.numberOfGenerations + 1):
                self.fitnessList[i][j] *= -1
                if self.fitnessList[i][j] < 0:
                    self.fitnessList[i][j] = 0

        np.save(f"data/fitnessValues{x}.npy", self.fitnessList)

        for i in range(len(self.fitnessList)):
            mpl.plot(self.fitnessList[i], label=f"member #{i + 1}")
        mpl.title(f"Fitness Over {c.numberOfGenerations} Generations, Seed #{x}")
        mpl.xlabel("Number of Generations")
        mpl.ylabel("Fitness")
        mpl.savefig(f"graphs/fitness{x}.png", format="png")

    def Find_Fittest(self):
        fittest = 0
        for i in self.parents:
            if self.parents[i].fitness < self.parents[fittest].fitness:
                fittest = i

        return fittest

    def Pickle_Solution(self, fittest):
        pickle.dump(self.parents[fittest], open(f"pickles/run{self.seed}_pickle{self.pickleCount}.pkl", "wb"))
        self.pickleCount += 1
        self.bestFitness = self.parents[fittest].fitness
