import constants as c
import bodyplan
import pyrosim.pyrosim as pyrosim

bp = bodyplan.BODY_PLAN()
print("calling create blueprint")
links, joints = bp.Create_Blueprint()


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.End()


def Create_Body():
    pyrosim.Start_URDF("body.urdf")

    for link in links:
        pyrosim.Send_Cube(name=link.name, pos=link.pos, size=link.size, rgba=link.rgba, colorName=link.colorName)

    for joint in joints:
        pyrosim.Send_Joint(name=joint.name, parent=joint.parent, child=joint.child, type="revolute",
                           position=joint.position, jointAxis=joint.jointAxis)

    pyrosim.End()


def Create_Brain():
    pyrosim.Start_NeuralNetwork(f"brain0.nndf")

    for i in range(len(links)):
        pyrosim.Send_Sensor_Neuron(name=i, linkName=links[i].name)

    for i in range(len(joints)):
        pyrosim.Send_Motor_Neuron(name=c.numSensorNeurons+i, jointName=joints[i].name)

    for currentRow in range(c.numSensorNeurons):
        for currentColumn in range(c.numMotorNeurons):
            pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
                                 weight=0)

    # pyrosim.Send_Sensor_Neuron(name=0, linkName="Base")
    # for i in range(c.numLinks):
    #     pyrosim.Send_Sensor_Neuron(name=i + 1, linkName=f"Link{i}")
    #
    # pyrosim.Send_Motor_Neuron(name=c.numSensorNeurons, jointName="Base_Link0")
    # for i in range(c.numLinks - 1):
    #     pyrosim.Send_Motor_Neuron(name=c.numSensorNeurons + i + 1, jointName=f"Link{i}_Link{i + 1}")
    #
    # for currentRow in range(c.numSensorNeurons):
    #     for currentColumn in range(c.numMotorNeurons):
    #         # if currentRow <= 1:
    #         #     pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
    #         #                          weight=self.weights[currentRow][(currentColumn + 1) // 2])
    #         # else:
    #         #     pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
    #         #                          weight=self.weights[(currentRow + 2) // 2][(currentColumn + 1) // 2])
    #         pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
    #                              weight=1)

    pyrosim.End()


Create_World()
Create_Body()
Create_Brain()
