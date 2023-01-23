import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName

    def Set_Value(self, desiredAngle, robotId):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=75)

    # def Save_Values(self):
    #     numpy.save("data/motorValues.npy", self.motorValues)
