import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitudeBL
        self.frequency = c.frequencyBL
        self.offset = c.phaseOffsetBL

        self.motorValues = numpy.linspace(0, 2 * numpy.pi, c.steps)
        for i in range(len(self.motorValues)):
            self.motorValues[i] = self.amplitude * numpy.sin(self.frequency * self.motorValues[i] + self.offset)

    def Set_Value(self, t, robotId):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[t],
            maxForce=75)
