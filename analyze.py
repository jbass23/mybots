import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
print(backLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.show()

frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
print(frontLegSensorValues)
matplotlib.pyplot.plot(frontLegSensorValues)
matplotlib.pyplot.show()