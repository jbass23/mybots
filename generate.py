import constants as c
import pyrosim.pyrosim as pyrosim
import random


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.End()


def Create_Body():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Base", pos=[0, 0, 0.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Base_Link0", parent="Base", child="Link0",
                       type="revolute", position=[-0.5, 0, 0.5], jointAxis="0 1 0")

    for i in range(10):
        # print(f"Link{i}")
        pyrosim.Send_Cube(name=f"Link{i}", pos=[-0.5, 0, 0], size=[1, 1, 1])

        if i + 1 < 10:
            # print(f"Link{i}_Link{i+1}")
            pyrosim.Send_Joint(name=f"Link{i}_Link{i + 1}", parent=f"Link{i}", child=f"Link{i + 1}",
                               type="revolute", position=[-1, 0, 0], jointAxis="0 1 0")

    pyrosim.End()


def Create_Brain():
    pyrosim.Start_NeuralNetwork(f"brain0.nndf")
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Base")
    for i in range(c.numLinks):
        pyrosim.Send_Sensor_Neuron(name=i + 1, linkName=f"Link{i}")

    pyrosim.Send_Motor_Neuron(name=c.numSensorNeurons, jointName="Base_Link0")
    for i in range(c.numLinks - 1):
        pyrosim.Send_Motor_Neuron(name=c.numSensorNeurons + i + 1, jointName=f"Link{i}_Link{i + 1}")

    for currentRow in range(c.numSensorNeurons):
        for currentColumn in range(c.numMotorNeurons):
            # if currentRow <= 1:
            #     pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
            #                          weight=self.weights[currentRow][(currentColumn + 1) // 2])
            # else:
            #     pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
            #                          weight=self.weights[(currentRow + 2) // 2][(currentColumn + 1) // 2])
            pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
                                 weight=1)

    pyrosim.End()


Create_World()
Create_Body()
Create_Brain()
