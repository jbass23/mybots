import constants as c
import pyrosim.pyrosim as pyrosim
import os
import numpy as np
import random
import time


class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = np.random.rand(c.numSensorNeurons//2 + 1, c.numMotorNeurons//2) * 2 - 1
        # self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1
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
        # pyrosim.Send_Cube(name="Step1", pos=[-4, 0, 0.0625], size=[2, 10, 0.125], mass=1000)
        # pyrosim.Send_Cube(name="Step2", pos=[-6, 0, 0.125], size=[2, 10, 0.25], mass=1000)
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[2, 1, 0.75])
        pyrosim.Send_Joint(name='Torso_FrontLeftLeg', parent="Torso", child="FrontLeftLeg",
                           type="revolute", position=[-0.5, -0.5, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontLeftLeg", pos=[-0.4, -0.1, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name='Torso_FrontRightLeg', parent="Torso", child="FrontRightLeg",
                           type="revolute", position=[-0.5, 0.5, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontRightLeg", pos=[-0.4, 0.1, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name='Torso_BackLeftLeg', parent="Torso", child="BackLeftLeg",
                           type="revolute", position=[0.5, -0.5, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="BackLeftLeg", pos=[0.4, -0.1, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name='Torso_BackRightLeg', parent="Torso", child="BackRightLeg",
                           type="revolute", position=[0.5, 0.5, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="BackRightLeg", pos=[0.4, 0.1, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name='FrontLeftLeg_FrontLeftLowerLeg', parent="FrontLeftLeg", child="FrontLeftLowerLeg",
                           type="revolute", position=[-0.9, -0.1, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontLeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name='FrontRightLeg_FrontRightLowerLeg', parent="FrontRightLeg", child="FrontRightLowerLeg",
                           type="revolute", position=[-0.9, 0.1, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontRightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name='BackLeftLeg_BackLeftLowerLeg', parent="BackLeftLeg", child="BackLeftLowerLeg",
                           type="revolute", position=[0.9, -0.1, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="BackLeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name='BackRightLeg_BackRightLowerLeg', parent="BackRightLeg", child="BackRightLowerLeg",
                           type="revolute", position=[0.9, 0.1, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="BackRightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="FrontLeftLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontRightLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="BackLeftLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="BackRightLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="FrontLeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="FrontRightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="BackLeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="BackRightLowerLeg")
        pyrosim.Send_Motor_Neuron(name=9, jointName='Torso_FrontLeftLeg')
        pyrosim.Send_Motor_Neuron(name=10, jointName='Torso_FrontRightLeg')
        pyrosim.Send_Motor_Neuron(name=11, jointName='Torso_BackLeftLeg')
        pyrosim.Send_Motor_Neuron(name=12, jointName='Torso_BackRightLeg')
        pyrosim.Send_Motor_Neuron(name=13, jointName='FrontLeftLeg_FrontLeftLowerLeg')
        pyrosim.Send_Motor_Neuron(name=14, jointName='FrontRightLeg_FrontRightLowerLeg')
        pyrosim.Send_Motor_Neuron(name=15, jointName='BackLeftLeg_BackLeftLowerLeg')
        pyrosim.Send_Motor_Neuron(name=16, jointName='BackRightLeg_BackRightLowerLeg')

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.numSensorNeurons,
                                     weight=self.weights[currentRow//2][currentColumn//2])
                # pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.numSensorNeurons,
                                    # weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        self.weights[random.randint(0, c.numSensorNeurons//2)][random.randint(0, c.numMotorNeurons//2 - 1)] = random.random() * 2 - 1
        # self.weights[random.randint(0, c.numSensorNeurons - 1)][random.randint(0, c.numMotorNeurons - 1)] = random.random() * 2 - 1

    def Set_ID(self, ID):
        self.myID = ID
