import numpy

steps = 1000

numLinks = numpy.random.randint(3, 9)   # excludes the base
numSensorNeurons = numLinks + 1
numMotorNeurons = numLinks

motorJointRange = 0.5

numberOfGenerations = 500
populationSize = 10
