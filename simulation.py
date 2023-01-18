from world import WORLD
from robot import ROBOT
import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time


class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        self.world = WORLD()
        self.robot = ROBOT()

        p.setGravity(0,0,-9.8)

        pyrosim.Prepare_To_Simulate(self.robot.robotId)

    def Run(self):
        for i in range(c.steps):
            print(i)

            p.stepSimulation()
            # c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            #
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex=self.robotId,
            #     jointName=b'Torso_BackLeg',
            #     controlMode=p.POSITION_CONTROL,
            #     targetPosition=c.targetAnglesBL[i],
            #     maxForce=75)
            #
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex=self.robotId,
            #     jointName=b'Torso_FrontLeg',
            #     controlMode=p.POSITION_CONTROL,
            #     targetPosition=c.targetAnglesFL[i],
            #     maxForce=75)

            time.sleep(1/2400)

    def __del__(self):
        p.disconnect()
