import numpy

steps = 1000

amplitudeBL = numpy.pi / 3
frequencyBL = 8
phaseOffsetBL = 0

amplitudeFL = numpy.pi / 3
frequencyFL = 4
phaseOffsetFL = 0

numLinks = numpy.random.randint(5, 15)

numSensorNeurons = numLinks + 1
numMotorNeurons = numLinks

numberOfGenerations = 0
populationSize = 1
motorJointRange = 0.5
