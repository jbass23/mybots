import numpy

steps = 1000

amplitudeBL = numpy.pi / 3
frequencyBL = 8
phaseOffsetBL = numpy.pi / 4

amplitudeFL = numpy.pi / 3
frequencyFL = 8
phaseOffsetFL = 0

targetAnglesBL = numpy.linspace(0, 2 * numpy.pi, steps)
for i in range(len(targetAnglesBL)):
    targetAnglesBL[i] = amplitudeBL * numpy.sin(frequencyBL * targetAnglesBL[i] + phaseOffsetBL)
numpy.save("data/targetAnglesBL.npy", targetAnglesBL)

targetAnglesFL = numpy.linspace(0, 2 * numpy.pi, steps)
for i in range(len(targetAnglesFL)):
    targetAnglesFL[i] = amplitudeFL * numpy.sin(frequencyFL * targetAnglesFL[i] + phaseOffsetFL)
numpy.save("data/targetAnglesFL.npy", targetAnglesFL)