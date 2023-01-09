import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
p.loadURDF("plane.urdf")
p.loadSDF("box.sdf")
for i in range(1000):
	p.stepSimulation()
	time.sleep(1/60)
	print(f"iteration #{i}")

p.disconnect()
