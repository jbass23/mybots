import numpy

steps = 1000

amplitudeBL = numpy.pi / 3
frequencyBL = 8
phaseOffsetBL = 0

amplitudeFL = numpy.pi / 3
frequencyFL = 4
phaseOffsetFL = 0

numLinks = numpy.random.randint(3, 9)   # excludes the base

numSensorNeurons = numLinks + 1
numMotorNeurons = numLinks

numberOfGenerations = 100
populationSize = 100
motorJointRange = 0.5
