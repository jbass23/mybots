import constants as c
import bodyplan
import pyrosim.pyrosim as pyrosim
import os
import numpy as np

bp = bodyplan.BODY_PLAN()
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
    sensorCount = 0

    for i in range(c.numSensorNeurons):
        if bp.sensorBoolArray[i] == 1:
            pyrosim.Send_Sensor_Neuron(name=sensorCount, linkName=f"Link{i}")
            sensorCount += 1

    for i in range(len(joints)):
        pyrosim.Send_Motor_Neuron(name=sensorCount + i, jointName=joints[i].name)

    weights = np.random.rand(sensorCount, c.numMotorNeurons) * 2 - 1

    for currentRow in range(sensorCount):
        for currentColumn in range(c.numMotorNeurons):
            pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + sensorCount,
                                 weight=weights[currentRow][currentColumn])

    pyrosim.End()


Create_World()
Create_Body()
Create_Brain()

os.system(f"python3 simulate.py GUI 0 2&>1")
