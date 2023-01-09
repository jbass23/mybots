import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

x = 0
y = 0
z = 0.5
length = 1
width = 1
height = 1

for r in range(5):
	for c in range(5):
		for i in range(10):
        		size_mod = 0.9 ** i
        		pyrosim.Send_Cube(name="Box", pos=[x-2+r,y-2+c,z+i], 
			 size=[length*size_mod,width*size_mod,height*size_mod])

pyrosim.End()
