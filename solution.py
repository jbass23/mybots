import constants as c
import bodyplan
import pyrosim.pyrosim as pyrosim
import os
import numpy as np
import random
import time


class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.sensorBoolArray = np.random.randint(2, size=c.numSensorNeurons)
        self.bp = bodyplan.BODY_PLAN()
        self.links, self.joints = self.bp.Create_Blueprint()

        self.sensorCount = np.sum(self.bp.sensorBoolArray)
        self.weights = np.random.rand(self.sensorCount, c.numMotorNeurons) * 2 - 1

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
        # links, joints = self.bp.Create_Blueprint()

        for link in self.links:
            pyrosim.Send_Cube(name=link.name, pos=link.pos, size=link.size, rgba=link.rgba, colorName=link.colorName)

        for joint in self.joints:
            pyrosim.Send_Joint(name=joint.name, parent=joint.parent, child=joint.child, type="revolute",
                               position=joint.position, jointAxis=joint.jointAxis)

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        sensorIndex = 0

        for i in range(c.numSensorNeurons):
            if self.bp.sensorBoolArray[i] == 1:
                pyrosim.Send_Sensor_Neuron(name=sensorIndex, linkName=f"Link{i}")
                sensorIndex += 1

        for i in range(len(self.joints)):
            pyrosim.Send_Motor_Neuron(name=sensorIndex+i, jointName=self.joints[i].name)

        for currentRow in range(sensorIndex):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+sensorIndex,
                                     weight=self.weights[currentRow][currentColumn])

    def Mutate(self):
        self.weights[random.randint(0, self.sensorCount - 1)][random.randint(0, c.numMotorNeurons - 1)] = random.random() * 2 - 1

    def Set_ID(self, ID):
        self.myID = ID
