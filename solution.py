import constants as c
import pyrosim.pyrosim as pyrosim
import os
import numpy as np
import random
import time


class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = np.random.rand(c.numSensorNeurons//2 + 1, c.numMotorNeurons//2 + 1) * 2 - 1
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
        pyrosim.Send_Cube(name="Step1", pos=[-4, 0, 0.0625], size=[2, 10, 0.125], mass=1000)
        pyrosim.Send_Cube(name="Step2", pos=[-6, 0, 0.125], size=[2, 10, 0.25], mass=1000)
        pyrosim.Send_Cube(name="Step3", pos=[-8, 0, 0.1875], size=[2, 10, 0.375], mass=1000)
        pyrosim.Send_Cube(name="Step4", pos=[-10, 0, 0.25], size=[2, 10, 0.5], mass=1000)
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1.5, 0.75])
        pyrosim.Send_Joint(name='Torso_FrontLeftLeg', parent="Torso", child="FrontLeftLeg",
                           type="revolute", position=[-0.25, -0.75, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontLeftLeg", pos=[-0.4, -0.1, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name='Torso_FrontRightLeg', parent="Torso", child="FrontRightLeg",
                           type="revolute", position=[-0.25, 0.75, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontRightLeg", pos=[-0.4, 0.1, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name='Torso_BackLeftLeg', parent="Torso", child="BackLeftLeg",
                           type="revolute", position=[0.25, -0.75, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="BackLeftLeg", pos=[0.4, -0.1, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name='Torso_BackRightLeg', parent="Torso", child="BackRightLeg",
                           type="revolute", position=[0.25, 0.75, 1], jointAxis="0 1 0")
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
        pyrosim.Send_Joint(name="Torso_Head", parent="Torso", child="Head", type="revolute",
                           position=[-0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="Head", pos=[-0.4, 0, 0], size=[0.8, 0.8, 0.6])
        pyrosim.Send_Joint(name='Head_HeadLeftLeg', parent="Head", child="HeadLeftLeg",
                           type="revolute", position=[-0.4, -0.4, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="HeadLeftLeg", pos=[-0.4, -0.1, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name='Head_HeadRightLeg', parent="Head", child="HeadRightLeg",
                           type="revolute", position=[-0.4, 0.4, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="HeadRightLeg", pos=[-0.4, 0.1, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name='HeadLeftLeg_HeadLeftLowerLeg', parent="HeadLeftLeg", child="HeadLeftLowerLeg",
                           type="revolute", position=[-0.9, -0.1, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="HeadLeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name='HeadRightLeg_HeadRightLowerLeg', parent="HeadRightLeg", child="HeadRightLowerLeg",
                           type="revolute", position=[-0.9, 0.1, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="HeadRightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="Head")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeftLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="FrontRightLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="BackLeftLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="BackRightLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="FrontLeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="FrontRightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="BackLeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=9, linkName="BackRightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=10, linkName="HeadLeftLeg")
        pyrosim.Send_Sensor_Neuron(name=11, linkName="HeadRightLeg")
        pyrosim.Send_Sensor_Neuron(name=12, linkName="HeadLeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=13, linkName="HeadRightLowerLeg")
        pyrosim.Send_Motor_Neuron(name=14, jointName="Torso_Head")
        pyrosim.Send_Motor_Neuron(name=15, jointName='Torso_FrontLeftLeg')
        pyrosim.Send_Motor_Neuron(name=16, jointName='Torso_FrontRightLeg')
        pyrosim.Send_Motor_Neuron(name=17, jointName='Torso_BackLeftLeg')
        pyrosim.Send_Motor_Neuron(name=18, jointName='Torso_BackRightLeg')
        pyrosim.Send_Motor_Neuron(name=19, jointName='FrontLeftLeg_FrontLeftLowerLeg')
        pyrosim.Send_Motor_Neuron(name=20, jointName='FrontRightLeg_FrontRightLowerLeg')
        pyrosim.Send_Motor_Neuron(name=21, jointName='BackLeftLeg_BackLeftLowerLeg')
        pyrosim.Send_Motor_Neuron(name=22, jointName='BackRightLeg_BackRightLowerLeg')
        pyrosim.Send_Motor_Neuron(name=23, jointName='Head_HeadLeftLeg')
        pyrosim.Send_Motor_Neuron(name=24, jointName='Head_HeadRightLeg')
        pyrosim.Send_Motor_Neuron(name=25, jointName='HeadLeftLeg_HeadLeftLowerLeg')
        pyrosim.Send_Motor_Neuron(name=26, jointName='HeadRightLeg_HeadRightLowerLeg')

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                if currentRow <= 1:
                    pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
                                         weight=self.weights[currentRow][(currentColumn + 1) // 2])
                else:
                    pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
                                         weight=self.weights[(currentRow + 2) // 2][(currentColumn + 1) // 2])
                # pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.numSensorNeurons,
                                     # weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        self.weights[random.randint(0, c.numSensorNeurons//2)][random.randint(0, c.numMotorNeurons//2)] = random.random() * 2 - 1
        # self.weights[random.randint(0, c.numSensorNeurons - 1)][random.randint(0, c.numMotorNeurons - 1)] = random.random() * 2 - 1

    def Set_ID(self, ID):
        self.myID = ID
