import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
matplotlib.pyplot.plot(frontLegSensorValues, label="back leg", linewidth=3)
matplotlib.pyplot.plot(backLegSensorValues, label="front leg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()