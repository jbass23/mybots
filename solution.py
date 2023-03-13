import constants as c
import bodyplan
import pyrosim.pyrosim as pyrosim
import os
import numpy as np
import time


class SOLUTION:
    def __init__(self, nextAvailableID):
        self.numLinks = c.numLinks
        self.numSensorNeurons = c.numSensorNeurons
        self.numMotorNeurons = c.numMotorNeurons

        self.myID = nextAvailableID
        self.sensorBoolArray = np.random.randint(2, size=self.numSensorNeurons)
        self.bp = bodyplan.BODY_PLAN()
        self.links, self.joints = self.bp.Create_Blueprint()

        self.sensorCount = np.sum(self.bp.sensorBoolArray)
        self.weights = np.random.rand(self.sensorCount, self.numMotorNeurons) * 2 - 1


    def Start_Simulation(self, directOrGUI, ampersand=True):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        if ampersand:
            os.system(f"python3 simulate.py {directOrGUI} {self.myID} 2&>1 &")
        else:
            os.system(f"python3 simulate.py {directOrGUI} {self.myID} 2&>1")

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
        pyrosim.Start_URDF(f"body{self.myID}.urdf")

        for link in self.links:
            pyrosim.Send_Cube(name=link.name, pos=link.pos, size=link.size, rgba=link.rgba, colorName=link.colorName)

        for joint in self.joints:
            pyrosim.Send_Joint(name=joint.name, parent=joint.parent, child=joint.child, type="revolute",
                               position=joint.position, jointAxis=joint.jointAxis)

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        sensorIndex = 0

        for i in range(self.numSensorNeurons):
            if self.bp.sensorBoolArray[i] == 1:
                pyrosim.Send_Sensor_Neuron(name=sensorIndex, linkName=f"Link{sensorIndex}")
                sensorIndex += 1

        for i in range(len(self.joints)):
            pyrosim.Send_Motor_Neuron(name=sensorIndex+i, jointName=self.joints[i].name)

        for currentRow in range(self.sensorCount):
            for currentColumn in range(self.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+self.sensorCount,
                                     weight=self.weights[currentRow][currentColumn])

    def Mutate(self):
        if self.fitness < -5:
            synapseChance = 1
            dimensionChance = 12
        elif self.fitness < -3:
            synapseChance = 2
            dimensionChance = 8
        else:
            synapseChance = 3
            dimensionChance = 4

        # mutate a random number of synapse weights
        if self.sensorCount != 0:
            motorMutates = 0
            odds = synapseChance / (self.sensorCount * self.numMotorNeurons)
            for row in range(self.sensorCount):
                for col in range(self.numMotorNeurons):
                    chance = np.random.rand()
                    if chance <= odds:
                        self.weights[row][col] = np.random.rand() * 2 - 1
                        motorMutates += 1

            # print(f"mutated {motorMutates} times")

        # mutate a random number of link dimensions
        failCount = 0
        mutateCount = 0
        for i in range(len(self.links)):
            for xyz in range(3):
                mutateChance = np.random.randint(dimensionChance)
                if mutateChance == 0:
                    mutated = self.bp.Mutate_Link_Size(i, xyz)
                    self.links = self.bp.links
                    self.joints = self.bp.joints
                    if not mutated:
                        failCount += 1
                    else:
                        mutateCount += 1

        # print(f"failed {failCount} times")
        # print(f"mutated {mutateCount} times")

    def Set_ID(self, ID):
        self.myID = ID
