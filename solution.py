import numpy.random

import constants as c
import pyrosim.pyrosim as pyrosim
import os
import numpy as np
import random
import time


class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1
        self.myID = nextAvailableID

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        os.system(f"python3 simulate.py {directOrGUI} {self.myID} 2&>1 &")

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists(f"fitness{self.myID}.txt"):
            time.sleep(0.01)
        f = open(f"fitness{self.myID}.txt", "r")
        self.fitness = float(f.read())
        f.close()

        os.system(f"rm fitness{self.myID}.txt")

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        baseSize = numpy.random.rand(3) * 1.5 + 0.5
        pyrosim.Send_Cube(name="Base", pos=[0, 0, 1], size=baseSize)
        pyrosim.Send_Joint(name="Base_Link0", parent="Base", child="Link0",
                           type="revolute", position=[baseSize[0] / -2, 0, 1], jointAxis="0 1 0")

        for i in range(c.numLinks):
            linkSize = numpy.random.rand(3) * 1.5 + 0.5
            pyrosim.Send_Cube(name=f"Link{i}", pos=[linkSize[0] / -2, 0, 0], size=linkSize)

            if i+1 < c.numLinks:
                pyrosim.Send_Joint(name=f"Link{i}_Link{i+1}", parent=f"Link{i}", child=f"Link{i+1}",
                                   type="revolute", position=[-1 * linkSize[0], 0, 0], jointAxis="0 1 0")

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Base")
        for i in range(c.numLinks):
            pyrosim.Send_Sensor_Neuron(name=i+1, linkName=f"Link{i}")

        pyrosim.Send_Motor_Neuron(name=c.numSensorNeurons, jointName="Base_Link0")
        for i in range(c.numLinks-1):
            pyrosim.Send_Motor_Neuron(name=c.numSensorNeurons+i+1, jointName=f"Link{i}_Link{i+1}")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        self.weights[random.randint(0, c.numSensorNeurons - 1)][random.randint(0, c.numMotorNeurons - 1)] = random.random() * 2 - 1

    def Set_ID(self, ID):
        self.myID = ID
