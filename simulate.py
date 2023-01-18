from simulation import SIMULATION

simulation = SIMULATION()
simulation.Run()

# import constants as c
# import pybullet as p
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# import numpy
# import time
# import random
#
# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
#
# p.setGravity(0,0,-9.8)
# p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")
#
# pyrosim.Prepare_To_Simulate(robotId)
#
# # exit()
# for i in range(c.steps):
# 	p.stepSimulation()
# 	c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
# 	c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#
# 	pyrosim.Set_Motor_For_Joint(
# 		bodyIndex=robotId,
# 		jointName=b'Torso_BackLeg',
# 		controlMode=p.POSITION_CONTROL,
# 		targetPosition=c.targetAnglesBL[i],
# 		maxForce=75)
#
# 	pyrosim.Set_Motor_For_Joint(
# 		bodyIndex=robotId,
# 		jointName=b'Torso_FrontLeg',
# 		controlMode=p.POSITION_CONTROL,
# 		targetPosition=c.targetAnglesFL[i],
# 		maxForce=75)
#
# 	time.sleep(1/2400)
#
# numpy.save("data/backLegSensorValues.npy", c.backLegSensorValues)
# numpy.save("data/frontLegSensorValues.npy", c.frontLegSensorValues)
# p.disconnect()
